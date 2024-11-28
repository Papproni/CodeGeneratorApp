import tkinter as tk
from tkinter import Canvas, Menu, StringVar, OptionMenu

# No parameter needed
# init:
# type: input
# Source: 
# numofInputs: 0
# number of channels per inputs: 0
# numofOutputs: 1
# number of channels per outputs: 1


class InputBlock:
    def __init__(self,canvas,tag,x=None,y=None):
        # default values
        self.type            = "INPUT_BLOCK"
        # must be changed 
        self.source          = "LOOP1_INPUT"
        self.tag             = tag

        # NO INPUT DEFINED
        self.input_num       = 0
        self.input_channel   = 0

        # ONE OUTPUT DEFINED
        self.output_num      = 1
        self.output_channel  = 1

        # Define the options for the dropdown menu
        self.options = ["FX In"]
         # Variable to hold the selected option
        self.selected_option = StringVar()
        self.selected_option.set(self.options[0])  # Set the default option
         # Create the dropdown menu
        self.dropdown = OptionMenu(canvas.master, self.selected_option, *self.options)

        # Create Block
        if(x is None):
            x = 50
            y = 50

        input_block     = canvas.create_rectangle(x, y, x+120, y+80, fill="lightblue", tags=("block", tag))
        input_text      = canvas.create_text(x+50, y+25, text="INPUT", font=("Arial", 14), tags=("block", tag))
        output_circle   = canvas.create_oval(x+110, y+15, x+130, y+35, fill="yellow", tags=("output_circle", tag))
        dropdown_window = canvas.create_window(x + 60, y + 60, window=self.dropdown, anchor="center", tags=("block", tag))

# No parameter needed
# init:
# type: input
# Source: 
# numofInputs: 1
# number of channels per inputs: 1
# numofOutputs: 0
# number of channels per outputs: 0


class OutputBlock:
    def __init__(self,canvas,tag,x=None,y=None):
        super().__init__()
        # default values
        self.type            = "OUTPUT_BLOCK"
        # must be changed 
        self.source          = "LOOP1_OUTPUT"
        self.tag             = tag

        # 1 INPUT DEFINED
        self.input_num       = 1
        self.input_channel   = 1
        
        # NO OUTPUT DEFINED
        self.output_num      = 0
        self.output_channel  = 0

        # Define the options for the dropdown menu
        self.options = ["FX Out"]

        # Create Block
        if(x is None):
            x = 50
            y = 50
        
         # Variable to hold the selected option
        self.selected_option = StringVar()
        self.selected_option.set(self.options[0])  # Set the default option
        
        # Create the dropdown menu
        self.dropdown = OptionMenu(canvas.master, self.selected_option, *self.options)

        output_block    = canvas.create_rectangle(x, y, x+120, y+80, fill="lightgreen", tags=("block", tag))
        output_text     = canvas.create_text(x+50, y+25, text="OUTPUT", font=("Arial", 14), tags=("block", tag))
        input_circle    = canvas.create_oval(x-10, y+15, x+10, y+35, fill="green", tags=("input_circle", tag))
        # Add the dropdown menu to the canvas, above the text
        dropdown_window = canvas.create_window(x + 60, y + 60, window=self.dropdown, anchor="center", tags=("block", tag))

    
    
