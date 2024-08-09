import tkinter as tk
from tkinter import Canvas, Menu

# No parameter needed
# init:
# type: input
# Source: 
# numofInputs: 0
# number of channels per inputs: 0
# numofOutputs: 1
# number of channels per inputs: 1


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

        # Create Block
        x = 50
        y = 50
        input_block     = canvas.create_rectangle(x, y, x+100, y+50, fill="lightblue", tags=("block", tag))
        input_text      = canvas.create_text(x+50, y+25, text="INPUT", font=("Arial", 14), tags=("block", tag))
        output_circle   = canvas.create_oval(x+90, y+15, x+110, y+35, fill="yellow", tags=("output_circle", tag))
        


    
    
