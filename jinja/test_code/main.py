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
template = env.get_template("template.jinja")

# 4. GENERATE FILES FROM TEMPLATE
# Generate files for each effect

# Fancy start with borders and color
print(f"{bcolors.OKGREEN}{bcolors.BOLD}" + "╔" + "═" * 48 + "╗")
print(f"║{bcolors.OKCYAN}{bcolors.BOLD}        Welcome to the Code Generation Tool        {bcolors.OKGREEN}║")
print(f"║{bcolors.OKBLUE}       Generating Header Files for Effects       {bcolors.OKGREEN}║")
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
