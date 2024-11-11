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
effects = [
    {
        "name": "delay",
        "variables": [
            {"name": "mix",         "type": "float32_t"},
            {"name": "time",        "type": "float32_t"},
            {"name": "feedback",    "type": "float32_t"}
        ]
    },
    {
        "name": "overdrive",
        "variables": [
            {"name": "gain", "type": "float32_t"},
            {"name": "tone", "type": "float32_t"},
            {"name": "volume", "type": "float32_t"}
        ]
    },
    {
        "name": "distortion",
        "variables": [
            {"name": "gain", "type": "float32_t"},
            {"name": "tone", "type": "float32_t"},
            {"name": "presence", "type": "float32_t"},
            {"name": "sag", "type": "float32_t"},
            {"name": "bass", "type": "float32_t"},
            {"name": "mid", "type": "float32_t"},
            {"name": "treble", "type": "float32_t"},
            {"name": "volume", "type": "float32_t"}
        ]
    },
    {
        "name": "octave",
        "variables": [
            {"name": "octave1_up_vol", "type": "float32_t"},
            {"name": "octave2_up_vol", "type": "float32_t"},
            {"name": "octave1_down_vol", "type": "float32_t"},
            {"name": "octave2_down_vol", "type": "float32_t"},
            {"name": "normal_vol", "type": "float32_t"}
        ]
    },
    {
        "name": "flanger",
        "variables": [
            {"name": "rate", "type": "float32_t"},
            {"name": "depth", "type": "float32_t"},
            {"name": "manual", "type": "float32_t"},
            {"name": "res", "type": "float32_t"}
        ]
    },
    {
        "name": "chorus",
        "variables": [
            {"name": "level", "type": "float32_t"},
            {"name": "rate", "type": "float32_t"},
            {"name": "filter", "type": "float32_t"},
            {"name": "depth", "type": "float32_t"}
        ]
    },
    {
        "name": "boost",
        "variables": [
            {"name": "boost", "type": "float32_t"}
        ]
    },
    {
        "name": "pitchshift",
        "variables": [
            {"name": "pitch", "type": "float32_t"},
            {"name": "mix", "type": "float32_t"},
            {"name": "vol", "type": "float32_t"}
        ]
    },
    {
        "name": "fuzz",
        "variables": [
            {"name": "sustain", "type": "float32_t"},
            {"name": "tone", "type": "float32_t"},
            {"name": "vol", "type": "float32_t"}
        ]
    },
    {
        "name": "tremolo",
        "variables": [
            {"name": "mix", "type": "float32_t"},
            {"name": "rate", "type": "float32_t"},
            {"name": "depth", "type": "float32_t"}
        ]
    },
    {
        "name": "equalizer",
        "variables": [
            {"name": "vol", "type": "float32_t"},
            {"name": "gain", "type": "float32_t"},
            {"name": "20hz", "type": "float32_t"},
            {"name": "40hz", "type": "float32_t"},
            {"name": "80hz", "type": "float32_t"},
            {"name": "160hz", "type": "float32_t"},
            {"name": "315hz", "type": "float32_t"},
            {"name": "630hz", "type": "float32_t"},
            {"name": "1.25khz", "type": "float32_t"},
            {"name": "2.5khz", "type": "float32_t"},
            {"name": "5khz", "type": "float32_t"},
            {"name": "10khz", "type": "float32_t"},
            {"name": "20khz", "type": "float32_t"}
        ]
    }
]



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

