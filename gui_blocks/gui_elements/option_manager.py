import tkinter as tk

class OptionManager:
    def __init__(self):
        self.option_vars = {}

    
    # add_option examples:
    #   Numeric parameter:
    #       self.add_option("LOW",  "NUM", -20000, 20000)
    #   Chooseable:
    #       self.add_option("TYPE", "OPTIONBOX", default_value="LPF,HPF,NOTCH,BANDPASS")
    def add_option(self, option_name, option_type, min_value=None, max_value=None, default_value="1", bindable=None, visible_on_block = None):
        
        # Handle option types: NUM (numeric entry) and OPTIONBOX (dropdown menu)
        if option_type == "NUM":
            # Create a StringVar to hold the value of the option
            var = tk.StringVar(value=default_value)
            self.option_vars[option_name] = {
                "var": var,
                "min_value": min_value,
                "max_value": max_value,
                "bindable": bindable,
                "default_value": default_value,
                "type":         option_type,
                "binded_src": None
            }
            var.trace_add("write", lambda *args, name=option_name: self.on_variable_change(name))
            if(False == visible_on_block):
                return
            self.inc_opt_counter()
            # Create the entry widget, bind it to the StringVar
            entry = tk.Entry(self.canvas, width=5, textvariable=var)

            # Display the option name on the canvas
            text = option_name.capitalize()
            
            self.create_option_widget(option_name, entry, "entry")

            
        elif option_type == "OPTIONBOX":
            # Split the comma-separated list into individual options
            options = default_value.split(",")
            # Create a StringVar to hold the selected option
            var = tk.StringVar(value=options[0])
            self.option_vars[option_name] = {
                "var": var,
                "min_value": min_value,
                "max_value": max_value,
                "bindable": bindable,
                "default_value": default_value,
                "type":         option_type
            }

            if(False == visible_on_block):
                return
            self.inc_opt_counter()

            # Create the OptionMenu (dropdown) widget
            option_menu = tk.OptionMenu(self.canvas, var, *options)

            # Display the option name on the canvas
            text = option_name.capitalize()
            
            self.create_option_widget(option_name, option_menu, "optionmenu")

        elif option_type == "TICKBOX":
            # Create a BooleanVar to hold the state of the tickbox (True/False)
            var = tk.BooleanVar(value=bool(int(default_value)))  # Convert default_value to boolean
            self.option_vars[option_name] = {"var": var,
                                             "bindable": bindable}

            if(False == visible_on_block):
                return
            self.inc_opt_counter()
            checkbutton = tk.Checkbutton(self.canvas, variable=var)
            text = option_name.capitalize()
            
            self.create_option_widget(option_name, checkbutton, "tickbox")

    def create_option_widget(self, option_name, widget, widget_type="entry"):
        # Create the text label for the option
        text = option_name.capitalize()
        self.canvas.create_text(
            self.x + 0.2 * self.w,
            self.y + self.opt_start_y + self.opt_height * self.opt_counter,
            text=text,
            font=("Arial", 14),
            tags=("block", self.tag)
        )

        # Create window for the widget (entry, optionmenu, etc.) in the canvas
        self.canvas.create_window(
            self.x + 0.7 * self.w,
            self.y + self.opt_start_y + self.opt_height * self.opt_counter,
            window=widget,
            tags=(f"{option_name}_{widget_type}", self.tag),
            anchor="center"
        )

    def on_variable_change(self, name):
        data = self.option_vars[name]
        self.validate_numeric_input(data)
        print("on_variable_change")

    def validate_numeric_input(self, data):

        value   = data.get('var').get()
        min_value       = data['min_value']
        max_value       = data['max_value']
        default_value   = data['default_value']
        try:
            num = float(value)  # Use float instead of int to handle floating-point numbers
            if min_value is not None and num < min_value:
                data.get('var').set(min_value)
                raise ValueError("Value is below the minimum limit")
            if max_value is not None and num > max_value:
                data.get('var').set(max_value)
                raise ValueError("Value is above the maximum limit")
        except ValueError:
            data.set(default_value)  # Reset to default if invalid

    def inc_opt_counter(self):
        self.opt_counter = self.opt_counter + 1

    def last_opt_added(self):
        self.opt_counter = self.opt_counter + 0.5