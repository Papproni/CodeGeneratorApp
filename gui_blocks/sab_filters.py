import tkinter as tk
from tkinter import Canvas, Menu

# FILTERBANK BLOCK------------------------------------------------------
# init:
# type: Filter
# Source: 
# numofInputs: 1
# number of channels per inputs: 1
# numofOutputs: 1
# number of channels per inputs: USER DEFINED
class FilterBank:
    def __init__(self,canvas,tag):
        # default values
        self.type            = "FILTERBANK_BLOCK"
        # must be changed 
        self.tag             = tag

        # NO INPUT DEFINED
        self.input_num       = 1
        self.input_channel   = 1

        # ONE OUTPUT DEFINED
        self.output_num      = 1
        self.output_channel  = 1

        # Create Block
        x = 50
        y = 50
        filterbank_block    = canvas.create_rectangle(x, y, x+100, y+50, fill="lightblue", tags=("block", tag))
        filterbank_text     = canvas.create_text(x+50, y+25, text="Filterbank", font=("Arial", 14), tags=("block", tag))
        input_circle        = canvas.create_oval(x-10, y+15, x+10, y+35, fill="green", tags=("input_circle", tag))
        output_circle       = canvas.create_oval(x+90, y+15, x+110, y+35, fill="yellow", tags=("output_circle", tag))
        
        # Add Entry Box for User Input
        self.entry = tk.Entry(canvas, width=5)
        self.entry.insert(0, "1")  # Default value
        self.entry.place(x=x+20, y=y+60)
        
        # Limit the input range (from 1 to 100)
        self.entry.bind("<FocusOut>", self.validate_input)
    
    def validate_input(self, event):
        value = self.entry.get()
        try:
            num = int(value)
            if num < 1 or num > 100:
                raise ValueError("Out of bounds")
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "1")  # Reset to default if invalid
#   ------------------------------------------------------

    
    
