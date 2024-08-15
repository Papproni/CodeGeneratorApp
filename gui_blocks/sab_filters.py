import tkinter as tk
from tkinter import Canvas, Menu, StringVar, OptionMenu

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
        filterbank_block    = canvas.create_rectangle(x, y, x+100, y+150, fill="lightblue",         tags=("block", tag))
        filterbank_text     = canvas.create_text(x+50, y+25, text="Filterbank", font=("Arial", 14), tags=("block", tag))
        input_circle        = canvas.create_oval(x-10, y+15, x+10, y+35, fill="green",              tags=("input_circle", tag))
        output_circle       = canvas.create_oval(x+90, y+15, x+110, y+35, fill="yellow",            tags=("output_circle", tag))
        
        # OPTIONS:
        #   ch:             filter channel num
        #   type:           lin = lin or log
        #   freq_start:     lowest frequency bin
        #   Q:              Filter characteristics              
        # NUMBER OF CHANNELS --------------------
        # Add Entry Box for User Input
        self.ch_entry = tk.Entry(canvas, width=5)
        self.ch_entry.insert(0, "1")  # Default value
        
        # Embed the entry widget into the canvas and tag it
        filterbank_chnum_text   = canvas.create_text(x+20, y+60, text="Bins", font=("Arial", 14), tags=("block", tag))
        self.ch_entry_window    = canvas.create_window(x + 70, y + 60, window=self.ch_entry, tags=("input_ch_entry", tag), anchor="center")
        
        # Filterbank Type --------------------
        # Define the options for the dropdown menu
        self.filterbank_step_options = ["Log","Lin"]
        self.selected_filterbank_step_option = StringVar()
        self.selected_filterbank_step_option.set(self.filterbank_step_options[0])  # Set the default option
        # Create the dropdown menu
        self.filterbank_step_opt_dropdown = OptionMenu(canvas.master, self.selected_filterbank_step_option, *self.filterbank_step_options)
        filterbank_step_opt_dropdown = canvas.create_window(x + 60,  y + 100, window=self.filterbank_step_opt_dropdown, anchor="center", tags=("block", tag))
        

        self.start_freq_entry = tk.Entry(canvas, width=5)
        self.start_freq_entry.insert(0, "1")  # Default value
        
        # Embed the entry widget into the canvas and tag it
        start_freq_entry_text   = canvas.create_text(x+20, y+120, text="Freq\n[Hz]", font=("Arial", 14), tags=("block", tag))
        self.start_freq_window  = canvas.create_window(x + 70, y + 120, window=self.start_freq_entry, tags=("input_freq_entry", tag), anchor="center")
        

        # Limit the input range (from 1 to 100)
        self.ch_entry.bind("<FocusOut>", self.validate_input)
        self.start_freq_entry.bind("<FocusOut>", self.freq_limits_check)
    
    def freq_limits_check(self, event):
        value = self.start_freq_entry.get()
        try:
            num = int(value)
            if num < 1 or num > 20000:
                raise ValueError("Out of bounds")
        except ValueError:
            self.start_freq_entry.delete(0, tk.END)
            self.start_freq_entry.insert(0, "1")  # Reset to default if invalid

    def validate_input(self, event):
        value = self.ch_entry.get()
        try:
            num = int(value)
            if num < 1 or num > 200:
                raise ValueError("Out of bounds")
        except ValueError:
            self.ch_entry.delete(0, tk.END)
            self.ch_entry.insert(0, "1")  # Reset to default if invalid
#   ------------------------------------------------------

    
    
