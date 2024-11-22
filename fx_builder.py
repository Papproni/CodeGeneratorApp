# This python lib creates the custom fx for the SABV3
import os
import shutil
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

import tkinter as tk

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
        self.template_fx_src = os.path.join(os.path.dirname(__file__),"/customfx_templates/effect_src_template.jinja")
        self.template_fx_inc = os.path.join(os.path.dirname(__file__),"/customfx_templates/effect_inc_template.jinja")
        self.block_template_path = os.path.join(os.path.dirname(__file__),"gui_blocks")
        self.templates_header, self.templates_init, self.templates_process = self.collect_template_files(self.block_template_path)
        self.output_dir = os.path.join(os.path.dirname(__file__),"/generated")
        

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
    
    def generate_code(self, paths,blocks,controls):
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

        # Step 2: Iterate through the signal path and generate code for each block
        for tag in paths[0]:
            # Ensure block_name exists in collected templates
            for block in blocks:
                if(block.tag == tag):
                    block_name = block.type
                    block_to_render = block
            if(block_name != 'INPUT_BLOCK' and block_name != 'OUTPUT_BLOCK'):
                
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
                self.render_and_save_template(header_template, block_to_render, header_output_path)

                # Render and save init file
                init_output_path = os.path.join(src_dir, f"{block_name}_init.c")
                self.render_and_save_template(init_template, block_to_render, init_output_path)

                # Render and save process file
                process_output_path = os.path.join(src_dir, f"{block_name}_process.c")
                self.render_and_save_template(process_template, block_to_render, process_output_path)

        # Step 3: Generate the top-level FX source file
        fx_src_output_path = os.path.join(src_dir, "fx_source.c")
        self.render_and_save_template(self.template_fx_src, params, fx_src_output_path)

        print("Code generation complete.")

    def render_and_save_template(self, template_path, block, output_path):
        """
        Render a Jinja template and save the output to a file.

        Parameters:
        - template_path (str): Path to the Jinja template file.
        - params (dict): Data to populate the template.
        - output_path (str): Path to save the rendered output.
        """
        # Load and render the template
        env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
        template = env.get_template(os.path.basename(template_path))
        rendered_content = template.render(block.option_vars)

        # Save the rendered content
        with open(output_path, "w") as f:
            f.write(rendered_content)
    
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
    
