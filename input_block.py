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
    def __init__(self,canvas,tag):
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
        self.options = ["Loop1 In", "Loop2 In", "Loop3 In", "Loop4 In"]
         # Variable to hold the selected option
        self.selected_option = StringVar()
        self.selected_option.set(self.options[0])  # Set the default option
         # Create the dropdown menu
        self.dropdown = OptionMenu(canvas.master, self.selected_option, *self.options)

        # Create Block
        x = 50
        y = 50
        input_block     = canvas.create_rectangle(x, y, x+120, y+80, fill="lightblue", tags=("block", tag))
        input_text      = canvas.create_text(x+50, y+25, text="INPUT", font=("Arial", 14), tags=("block", tag))
        output_circle   = canvas.create_oval(x+110, y+15, x+130, y+35, fill="yellow", tags=("output_circle", tag))
        dropdown_window = canvas.create_window(x + 60, y + 60, window=self.dropdown, anchor="center", tags=("block", tag))


    
    
