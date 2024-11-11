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

generated_libs_counter = 0
total_length = 35
# 1. SET DATA
# List of effects with multiple variables

import json

effects = [
    # Your effects data here
]

effect_path = os.path.join(os.path.dirname(__file__),"effects.json")

with open(effect_path, "r") as f:
    effects = json.load(f)

# 2. SET OUTPUT PARAMETERS
# Ensure the 'generated' directory exists
output_dir_inc = os.path.join(os.path.dirname(__file__), "generated/Inc")
os.makedirs(output_dir_inc, exist_ok=True)

output_dir_src = os.path.join(os.path.dirname(__file__), "generated/Src")
os.makedirs(output_dir_src, exist_ok=True)

current_date = datetime.now().strftime("%Y.%m.%d.")

# 3. SET TEMPLATES
# Load the template from the 'templates' directory
template_dir = os.path.join(os.path.dirname(__file__), "templates")
env = Environment(loader=FileSystemLoader(template_dir))
template_inc = env.get_template("effect_inc_template.jinja")
template_src = env.get_template("effect_src_template.jinja")

# 4. GENERATE FILES FROM TEMPLATE
# Generate files for each effect

# Fancy start with borders and color

print(f"\n\r{bcolors.OKGREEN}{bcolors.BOLD}" + "╔" + "═" * 48 + "╗")
print(f"║{bcolors.OKCYAN}{bcolors.BOLD}     STM Audio Board V3 Code Generator GUI      {bcolors.OKGREEN}║")
print(f"║{bcolors.OKBLUE}      Generating Header Files for Effects       {bcolors.OKGREEN}║")
print(f"{bcolors.OKGREEN}{bcolors.BOLD}" + "╚" + "═" * 48 + "╝" + f"{bcolors.ENDC}")

# EFFECT MANAGER TEMPLATE GENERATION!
print("\n\rGenerating individual effects libs:")

for effect in effects:
    # File name to be created in the 'generated' directory
    filename_inc = os.path.join(output_dir_inc, f"SAB_{effect['name'].lower()}.h")

    # Render template with effect data
    content = template_inc.render(effect, date=current_date)

    # Write rendered content to the generated file
    with open(filename_inc, mode="w", encoding="utf-8") as message:
        message.write(content)
        generated_libs_counter = generated_libs_counter + 1
        file_name = f"SAB_{effect['name'].lower()}.h"
        status =  "DONE!"
        dots = '.' * (total_length - len(file_name) - len(status))
        print(f"File {generated_libs_counter}: {file_name}{dots}{bcolors.OKGREEN}{status}{bcolors.ENDC}")
    # File name to be created in the 'generated' directory
    filename_src = os.path.join(output_dir_src, f"SAB_{effect['name'].lower()}.h")

    # Render template with effect data
    content = template_src.render(effect, date=current_date)

    # Write rendered content to the generated file
    with open(filename_src, mode="w", encoding="utf-8") as message:
        message.write(content)
        generated_libs_counter = generated_libs_counter + 1
        file_name = f"SAB_{effect['name'].lower()}.c"
        status =  "DONE!"
        dots = '.' * (total_length - len(file_name) - len(status))
        print(f"File {generated_libs_counter}: {file_name}{dots}{bcolors.OKGREEN}{status}{bcolors.ENDC}")

# EFFECT MANAGER TEMPLATE GENERATION!
print("\n\rGenerating manager lib:")

# MANAGER DATA
manager_data = [
    {
        "lib_name": "fx_manager",
        "effects": [
        ]
    }   
]

for effect in effects:
    # Extract the name and add it to the manager_data effects list
    manager_data[0]["effects"].append({"name": effect["name"]})


# add_effects_to_manager(effects,manager_data)
template_manager = env.get_template("effect_manager_template.jinja")

filename = os.path.join(output_dir_inc, f"SAB_fx_manager.h")
# lib_name = manager_data[0].get("name"),
content = template_manager.render(manager_data[0], date=current_date)

with open(filename, mode="w", encoding="utf-8") as message:
    # message.write(content)
    # generated_libs_counter = generated_libs_counter + 1
    # print(f"File {generated_libs_counter}: SAB_fx_manager.h".ljust(35)+bcolors.OKGREEN + "DONE!" + bcolors.ENDC)
    
    message.write(content)
    generated_libs_counter = generated_libs_counter + 1
    file_name = f"SAB_{manager_data[0]['lib_name'].lower()}.h"
    status =  "DONE!"
    dots = '.' * (total_length - len(file_name) - len(status))
    print(f"File {generated_libs_counter}: {file_name}{dots}{bcolors.OKGREEN}{status}{bcolors.ENDC}")


print("")
print(f"{bcolors.BOLD}{bcolors.OKGREEN}Code generation finished:{bcolors.ENDC}")
print(f"{bcolors.OKGREEN} {generated_libs_counter} files are generated!{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}Output dir: \n\r{output_dir_inc}{bcolors.ENDC}")

