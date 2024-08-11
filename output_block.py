import tkinter as tk
from tkinter import Canvas, Menu, StringVar, OptionMenu

# No parameter needed
# init:
# type: input
# Source: 
# numofInputs: 0
# number of channels per inputs: 0
# numofOutputs: 1
# number of channels per inputs: 1


class OutputBlock:
    def __init__(self,canvas,tag):
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
        options = ["Loop1 Out", "Loop2 Out", "Loop3 Out", "Loop4 Out"]

        # Create Block
        x = 200
        y = 50
        output_block    = canvas.create_rectangle(x, y, x+100, y+150, fill="lightgreen", tags=("block", tag))
        output_text     = canvas.create_text(x+50, y+25, text="OUTPUT", font=("Arial", 14), tags=("block", tag))
        input_circle    = canvas.create_oval(x-10, y+15, x+10, y+35, fill="green", tags=("input_circle", tag))
         # Variable to hold the selected option
        self.selected_option = StringVar()
        self.selected_option.set(options[0])  # Set the default option
        
        # Create the dropdown menu
        dropdown = OptionMenu(canvas.master, self.selected_option, *options)

        # Add the dropdown menu to the canvas, above the text
        dropdown_window = canvas.create_window(x + 50, y + 80, window=dropdown, anchor="center")
