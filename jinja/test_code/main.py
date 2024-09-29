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
    }
]



# 2. SET OUTPUT PARAMETERS
# Ensure the 'generated' directory exists
output_dir = os.path.join(os.path.dirname(__file__), "generated")
os.makedirs(output_dir, exist_ok=True)
current_date = datetime.now().strftime("%Y.%m.%d.")

# 3. SET TEMPLATES
# Load the template from the 'templates' directory
template_dir = os.path.join(os.path.dirname(__file__), "templates")
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template("effect_lib_template.jinja")

# 4. GENERATE FILES FROM TEMPLATE
# Generate files for each effect

# Fancy start with borders and color
print("")
print(f"{bcolors.OKGREEN}{bcolors.BOLD}" + "╔" + "═" * 48 + "╗")
print(f"║{bcolors.OKCYAN}{bcolors.BOLD}     STM Audio Board V3 Code Generator GUI      {bcolors.OKGREEN}║")
print(f"║{bcolors.OKBLUE}      Generating Header Files for Effects       {bcolors.OKGREEN}║")
print(f"{bcolors.OKGREEN}{bcolors.BOLD}" + "╚" + "═" * 48 + "╝" + f"{bcolors.ENDC}")


for effect in effects:
    # File name to be created in the 'generated' directory
    filename = os.path.join(output_dir, f"SAB_{effect['name'].lower()}.h")

    # Render template with effect data
    content = template.render(effect, date=current_date)

    # Write rendered content to the generated file
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"SAB_{effect['name'].lower()}.h".ljust(20)+bcolors.OKGREEN + "DONE!" + bcolors.ENDC)
        generated_libs_counter = generated_libs_counter + 1

# EFFECT MANAGER TEMPLATE GENERATION!
print("Generating manager lib")

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
template = env.get_template("effect_manager_template.jinja")

filename = os.path.join(output_dir, f"SAB_fx_manager.h")
content = template.render(manager_data = manager_data, date=current_date)

with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)
    print(f"SAB_fx_manager.h".ljust(20)+bcolors.OKGREEN + "DONE!" + bcolors.ENDC)
    generated_libs_counter = generated_libs_counter + 1

print("")
print(f"{bcolors.BOLD}{bcolors.OKGREEN}Code generation finished:{bcolors.ENDC}")
print(f"{bcolors.OKCYAN} {generated_libs_counter} files are generated{bcolors.ENDC}")

