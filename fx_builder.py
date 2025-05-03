# This python lib creates the custom fx for the SABV3
import os
import shutil
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

import tkinter as tk
import networkx as nx


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class SAB_fx_builder():
    def __init__(self):
        self.template_fx_src = os.path.join(os.path.dirname(__file__),"customfx_templates/effect_src_template.jinja")
        self.template_fx_inc = os.path.join(os.path.dirname(__file__),"customfx_templates/effect_inc_template.jinja")
        self.block_template_path = os.path.join(os.path.dirname(__file__),"gui_blocks")
        self.templates_header, self.templates_init, self.templates_process = self.collect_template_files(self.block_template_path)
        self.output_dir = os.path.join(os.path.dirname(__file__),"generated")

        self.myvar= os.path.dirname(__file__)
        

    def collect_template_files(self,base_path):
        templates_header = {}
        templates_init = {}
        templates_process = {}
        missing_templates = []
        
        jinja_templates_path = os.path.join(base_path, 'jinja_templates')
        if not os.path.exists(jinja_templates_path):
            raise FileNotFoundError(f"Folder 'jinja_templates' not found in {base_path}.")
        
        # Get subfolders in 'jinja_templates'
        subfolders = [f for f in os.listdir(jinja_templates_path) if os.path.isdir(os.path.join(jinja_templates_path, f))]
        print(f"Found {len(subfolders)} subfolders in 'jinja_templates'.")
        
        for subfolder in subfolders:
            subfolder_path = os.path.join(jinja_templates_path, subfolder)
            
            # Collect templates from each subfolder
            current_templates = {"header": None, "init": None, "process": None}
            for sub_subfolder, templates_dict, key in [
                ('header', templates_header, "header"),
                ('init', templates_init, "init"),
                ('process', templates_process, "process")
            ]:
                sub_subfolder_path = os.path.join(subfolder_path, sub_subfolder)
                if os.path.exists(sub_subfolder_path):
                    for file_name in os.listdir(sub_subfolder_path):
                        if file_name.endswith(".jinja"):
                            # Extract the identifier (e.g., "BIQUAD_FILTER")
                            file_identifier = file_name.split('_template_')[0].lower()
                            file_path = os.path.join(sub_subfolder_path, file_name)
                            templates_dict[file_identifier] = file_path
                            current_templates[key] = file_identifier
        return templates_header, templates_init, templates_process
    
    def build_pert_graph(self, arrows):
        """
        Build a PERT graph (DAG) from the given paths.
        """
        # G = nx.DiGraph()
        G = nx.MultiDiGraph()
        for arrow in arrows:
            G.add_edge(arrow[4],arrow[3])
        return G

    def execute_blocks_with_predecessors(self, graph):
        """
        Execute blocks in topological order using NetworkX built-ins.
        """
        for block in nx.topological_sort(graph):
            # Use built-in predecessors method
            predecessors = list(graph.predecessors(block))
            if predecessors:
                print(f"Execute {block}, \tpre: {', '.join(predecessors)}")
            else:
                print(f"Execute {block}, pre: None")
    
    def generate_code(self, arrows, blocks, controls, output_path_src, output_path_inc):
        """
        Generate code for each item in the signal path, using templates and parameters.

        Parameters:
        - signal_path (dict): A dictionary where keys are block types (e.g., "biquad_filter") and values are details.
        - params (dict): A dictionary containing data to fill Jinja templates.
        """
        # Step 1: Clean output directory and create necessary folders
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)
        os.makedirs(self.output_dir)
        inc_dir = os.path.join(self.output_dir, "inc")
        src_dir = os.path.join(self.output_dir, "src")
        os.makedirs(inc_dir)
        os.makedirs(src_dir)


        # Create controls
        controls_for_jinja = []
        
        for control in controls:
            control_list = {}
            for setting_name in controls[control]['settings']:
                setting_value = controls[control]['settings'][setting_name].get()
                control_list[setting_name] = setting_value
            
            controls_for_jinja.append(control_list)
        

        rendered_inits = []
        rendered_headers = []
        rendered_processes = []


        pert_graph = self.build_pert_graph(arrows)
        # Execute the blocks and print the predecessors
        
        # self.execute_blocks_with_predecessors(pert_graph)
        block_map = {block.tag: block for block in blocks}
        for tag in nx.topological_sort(pert_graph):
            # Use built-in predecessors method
            predecessors = list(pert_graph.predecessors(tag))
            if predecessors:
                print(f"Execute {tag}, \tpre: {', '.join(predecessors)}")
            else:
                print(f"Execute {tag}, pre: None")
            pre_to_render = []
            for block in blocks:
                for pre in predecessors:
                    if block.tag == pre:
                        count = pert_graph.number_of_edges(block.tag, tag)
                        for i in range(count):
                            pre_to_render.append(f'{block.type}_{block.tag}')
                if(block.tag == tag):
                    block_name = block.type
                    block_to_render = block
                
            block_key = block_name.lower()
            if block_key not in self.templates_header:
                raise FileNotFoundError(f"Missing header template for block '{block_name}'.")
            if block_key not in self.templates_init:
                raise FileNotFoundError(f"Missing init template for block '{block_name}'.")
            if block_key not in self.templates_process:
                raise FileNotFoundError(f"Missing process template for block '{block_name}'.")

            # Generate files using templates
            header_template = self.templates_header[block_key]
            init_template = self.templates_init[block_key]
            process_template = self.templates_process[block_key]

            # Render and save header file
            header_output_path = os.path.join(inc_dir, f"{block_name}_header.h")
            rendered_headers.append(self.render_and_save_template(header_template, block_to_render, pre_to_render))

            # Render and save init file
            rendered_inits.append(self.render_and_save_template(init_template, block_to_render,pre_to_render))

            # Render and save process file
            rendered_processes.append(self.render_and_save_template(process_template, block_to_render, pre_to_render))

        # Step 2: Iterate through the signal path and generate code for each block
            

        # Step 3: Generate the top-level FX source file
        if(output_path_inc == None):
            fx_inc_output_path = os.path.join(inc_dir, "SAB_custom_fx.h")
        else:
            fx_inc_output_path = os.path.join(output_path_inc, "SAB_custom_fx.h")

        if(output_path_src == None):
            fx_src_output_path = os.path.join(src_dir, "SAB_custom_fx.c")
        else:
            fx_src_output_path = os.path.join(output_path_src, "SAB_custom_fx.c")


        name = "custom_fx"
        # Load and render the template
        env = Environment(loader=FileSystemLoader(os.path.dirname(self.template_fx_inc)))
        template = env.get_template(os.path.basename(self.template_fx_inc))
        rendered_content = template.render(name =name, generated_outputs = rendered_headers,control_params = controls_for_jinja)
        # Save the rendered content
        with open(fx_inc_output_path, "w") as f:
            f.write(rendered_content)

        
        # Load and render the template
        env = Environment(loader=FileSystemLoader(os.path.dirname(self.template_fx_src)))
        template = env.get_template(os.path.basename(self.template_fx_src))
        rendered_content = template.render(name =name,
                                           generated_init_outputs = rendered_inits,
                                             generated_process_outputs = rendered_processes,
                                            control_params = controls_for_jinja)
        # Save the rendered content
        with open(fx_src_output_path, "w") as f:
            f.write(rendered_content)

        print("Code generation complete.")

    def render_and_save_template(self, template_path, block, pre_instances):
        """
        Render a Jinja template and save the output to a file.

        Parameters:
        - template_path (str): Path to the Jinja template file.
        - params (dict): Data to populate the template.
        """
        # Load and render the template
        env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
        template = env.get_template(os.path.basename(template_path))

        template_data = {}
        try:
            block.fill_template_data(template_data)
        except:
            pass
            # print("NO fill_template_data found while generating: {block.tag} | {block.type}")

        template_data['blockID'] = block.tag
        template_data['blocktype'] = block.type
        template_data['instance_name'] = f'{block.type}_{block.tag}'
        template_data['bind'] = None
        try:
            for key, data in block.option_vars.items():
                opt_name = key  # Extract the name of the option
                opt_value = data['var'].get()  # Extract the value of the option
                try:
                    if(data['binded_src'] != None):
                        template_data['bind'] = True
                except:
                    pass
                template_data[opt_name] = opt_value  # Add the key-value pair to the template
        except:
            pass

        rendered_content = template.render(template_data, pre_instances = pre_instances)

        return rendered_content
    
    def gen_code(self,paths,blocks,controls):
        pass


def add_option(params, option_name, option_type, min_value=None, max_value=None, default_value="1", bindable=None, visible_on_block = None):
    var = tk.StringVar(value=default_value)
    params = [option_name] = {
        "var": var,
        "min_value": min_value,
        "max_value": max_value,
        "bindable": bindable,
        "default_value": default_value,
        "type":         option_type,
        "binded_src": None
    }
    
if __name__ == "__main__":
    builder = SAB_fx_builder()
    # Example usage

    base_path = os.path.join(os.path.dirname(__file__),"gui_blocks")
    templates_header, templates_init, templates_process= builder.collect_template_files(base_path)

    blocktype = "BiquadFilter"
    blockID = 1
    signal_path = ['BIQUAD_FILTER']
    
    params = {}
    

    
    builder.generate_code(signal_path, params)
    print(templates_header)
    print(templates_init)
    print(templates_process)
    
