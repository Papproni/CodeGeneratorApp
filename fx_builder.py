# This python lib creates the custom fx for the SABV3
import os
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

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

class SAB_fx_builder:
    def __init__(self):
        self.generated_libs_counter = 0 
        total_length = 35

        # 
        self.path = {}

    def collect_template_files(self,base_path):
        """
        Collects and organizes template file paths into dictionaries based on file types.

        Parameters:
        base_path (str): The root directory path containing the 'jinja_templates' folder.

        Returns:
        tuple: Three dictionaries (`templates_header`, `templates_init`, `templates_process`) with file identifiers as keys and file paths as values.
        """
        templates_header = {}
        templates_init = {}
        templates_process = {}
        
        jinja_templates_path = os.path.join(base_path, 'jinja_templates')
        if not os.path.exists(jinja_templates_path):
            raise FileNotFoundError(f"Folder 'jinja_templates' not found in {base_path}.")
        
        # Get subfolders in 'jinja_templates'
        subfolders = [f for f in os.listdir(jinja_templates_path) if os.path.isdir(os.path.join(jinja_templates_path, f))]
        print(f"Found {len(subfolders)} subfolders in 'jinja_templates'.")
        
        for subfolder in subfolders:
            subfolder_path = os.path.join(jinja_templates_path, subfolder)
            
            for sub_subfolder, templates_dict in [
                ('header', templates_header),
                ('init', templates_init),
                ('process', templates_process)
            ]:
                sub_subfolder_path = os.path.join(subfolder_path, sub_subfolder)
                if os.path.exists(sub_subfolder_path):
                    for file_name in os.listdir(sub_subfolder_path):
                        if file_name.endswith(".jinja"):
                            # Extract the identifier (e.g., "BIQUAD_FILTER")
                            file_identifier = file_name.split('_template_')[0]
                            file_path = os.path.join(sub_subfolder_path, file_name)
                            templates_dict[file_identifier] = file_path
        
        return templates_header, templates_init, templates_process


if __name__ == "__main__":
    builder = SAB_fx_builder()
    # Example usage

    base_path = os.path.join(os.path.dirname(__file__),"gui_blocks")
    templates_header, templates_init, templates_process = builder.collect_template_files(base_path)
    print(templates_header)
    print(templates_init)
    print(templates_process)
    
