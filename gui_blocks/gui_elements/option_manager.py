import tkinter as tk

class OptionManager:
    # add_option examples:
    #   Numeric parameter:
    #       self.add_option("LOW",  "NUM", -20000, 20000)
    #   Chooseable:
    #       self.add_option("TYPE", "OPTIONBOX", default_value="LPF,HPF,NOTCH,BANDPASS")
    def add_option(self, option_name, option_type, min_value=None, max_value=None, default_value="1", bindable=None):
        self.inc_opt_counter()

        # Handle option types: NUM (numeric entry) and OPTIONBOX (dropdown menu)
        if option_type == "NUM":
            # Create a StringVar to hold the value of the option
            var = tk.StringVar(value=default_value)
            self.option_vars[option_name] = var

            # Create the entry widget, bind it to the StringVar
            entry = tk.Entry(self.canvas, width=5, textvariable=var)

            # Display the option name on the canvas
            text = option_name.capitalize()
            self.canvas.create_text(
                self.x + 0.2 * self.w,
                self.y + self.opt_start_y + self.opt_height * self.opt_counter,
                text=text,
                font=("Arial", 14),
                tags=("block", self.tag)
            )

            # Create window for the entry widget in the canvas
            self.canvas.create_window(
                self.x + 0.7 * self.w,
                self.y + self.opt_start_y + self.opt_height * self.opt_counter,
                window=entry,
                tags=(f"{option_name}_entry", self.tag),
                anchor="center"
            )

            # Bind the validation based on the option type
            entry.bind("<FocusOut>", lambda event, e=entry: self.validate_numeric_input(e, var, min_value, max_value, default_value))

        elif option_type == "OPTIONBOX":
            # Split the comma-separated list into individual options
            options = default_value.split(",")
            # Create a StringVar to hold the selected option
            var = tk.StringVar(value=options[0])
            self.option_vars[option_name] = var

            # Create the OptionMenu (dropdown) widget
            option_menu = tk.OptionMenu(self.canvas, var, *options)

            # Display the option name on the canvas
            text = option_name.capitalize()
            self.canvas.create_text(
                self.x + 0.2 * self.w,
                self.y + self.opt_start_y + self.opt_height * self.opt_counter,
                text=text,
                font=("Arial", 14),
                tags=("block", self.tag)
            )

            # Create window for the OptionMenu widget in the canvas
            self.canvas.create_window(
                self.x + 0.7 * self.w,
                self.y + self.opt_start_y + self.opt_height * self.opt_counter,
                window=option_menu,
                tags=(f"{option_name}_optionmenu", self.tag),
                anchor="center"
            )

    def validate_numeric_input(self, entry, var, min_value, max_value, default_value):
        value = var.get()
        try:
            num = int(value)
            if min_value is not None and num < min_value:
                raise ValueError("Value is below the minimum limit")
            if max_value is not None and num > max_value:
                raise ValueError("Value is above the maximum limit")
        except ValueError:
            var.set(default_value)  # Reset to default if invalid
            entry.delete(0, tk.END)
            entry.insert(0, default_value)

    def inc_opt_counter(self):
        self.opt_counter = self.opt_counter + 1

    def last_opt_added(self):
        self.opt_counter = self.opt_counter + 0.5