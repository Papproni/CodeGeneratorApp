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
        self.canvas = canvas

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
        self.x = 50
        self.y = 50
        self.w = 125
        self.io_circle_radius = 10
        
        # Option params
        self.opt_start_y    = 20
        self.opt_height     = 50 # pixel
        self.opt_counter    = 0
        self.opt_text_start = 20 # 20%
        self.opt_box_start  = 70 # 70%
        
        
        # self.filterbank_block    = canvas.create_rectangle(x, y, x+100, y+75+option_height*3, fill="red",         tags=("block", tag,"background"))
        self.filterbank_text_bg  = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+40, fill="grey",         tags=("block", self.tag,"text_background"))
        self.filterbank_text     = self.canvas.create_text(     self.x+self.w/2,    self.y+20, text="Filterbank", font=("Arial", 14), tags=("block", self.tag) )
        
        self.input_circle        = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+15, self.x+10, self.y+35, fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+15, self.x+self.w+10, self.y+35, fill="yellow",            tags=("output_circle", self.tag))
        
        # OPTIONS:
        #   ch:             filter channel num
        #   type:           lin = lin or log
        #   freq_start:     lowest frequency bin
        #   Q:              Filter characteristics              
        self.add_option_bins()
        self.add_option_freq()
        self.add_option_q()
        self.add_option_step()
        
        self.last_opt_added()
        self.filterbank_block    = self.canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.opt_start_y+self.opt_height*self.opt_counter, fill="red",         tags=("block", self.tag,"background"))
        canvas.tag_lower("background",'all')
    
    def add_option_q(self):
        self.inc_opt_counter()
        self.Q_entry               = tk.Entry(self.canvas, width=5)
        self.Q_entry.insert(0, "0.707")  # Default value
        self.filterbank_chnum_text  = self.canvas.create_text(self.x+0.2*self.w, self.y+self.opt_start_y+self.opt_height*self.opt_counter, text="Q", font=("Arial", 14), tags=("block", self.tag))
        self.Q_entry_window        = self.canvas.create_window(self.x + 0.7*self.w, self.y + self.opt_start_y+self.opt_height*self.opt_counter, window=self.Q_entry, tags=("input_Q_entry", self.tag), anchor="center")
        # Limit the input range (from 1 to 100)
        self.Q_entry.bind("<FocusOut>", self.validate_Q_input)
    
    def validate_Q_input(self):
        value = self.Q_entry.get()
        try:
            num = int(value)
            if num < 0.01 or num > 10:
                raise ValueError("Out of bounds")
        except ValueError:
            self.ch_entry.delete(0, tk.END)
            self.ch_entry.insert(0, "0.707")  # Reset to default if invalid

    def add_option_bins(self):
        self.inc_opt_counter()
        self.ch_entry = tk.Entry(self.canvas, width=5)
        self.ch_entry.insert(0, "1")  # Default value
        self.filterbank_chnum_text  = self.canvas.create_text(self.x+0.2*self.w, self.y+self.opt_start_y+self.opt_height*self.opt_counter, text="Bins", font=("Arial", 14), tags=("block", self.tag))
        self.ch_entry_window        = self.canvas.create_window(self.x + 0.7*self.w, self.y + self.opt_start_y+self.opt_height*self.opt_counter, window=self.ch_entry, tags=("input_ch_entry", self.tag), anchor="center")
        # Limit the input range (from 1 to 100)
        self.ch_entry.bind("<FocusOut>", self.validate_input)

    def add_option_step(self):
        self.inc_opt_counter()
        self.filterbank_step_options = ["Log","Lin"]
        self.selected_filterbank_step_option = StringVar()
        self.selected_filterbank_step_option.set(self.filterbank_step_options[0])  # Set the default option
        # Create the dropdown menu
        
        self.filterbank_step_opt_dropdown = OptionMenu(self.canvas.master, self.selected_filterbank_step_option, *self.filterbank_step_options)
        filterbank_step_opt_dropdown = self.canvas.create_window(self.x + self.w/2,  self.y + self.opt_start_y+self.opt_height*self.opt_counter, window=self.filterbank_step_opt_dropdown, anchor="center", tags=("block", self.tag))
        
    def add_option_freq(self):
        self.inc_opt_counter()
        self.start_freq_entry = tk.Entry(self.canvas, width=5)
        self.start_freq_entry.insert(0, "1")  # Default value
        
        # Embed the entry widget into the canvas and tag it
        start_freq_entry_text   = self.canvas.create_text(self.x+0.2*self.w, self.y+self.opt_start_y+self.opt_height*self.opt_counter, text="Freq\n[Hz]", font=("Arial", 14), tags=("block", self.tag))
        self.start_freq_window  = self.canvas.create_window(self.x + 0.7*self.w, self.y + self.opt_start_y+self.opt_height*self.opt_counter, window=self.start_freq_entry, tags=("input_freq_entry", self.tag), anchor="center")
        
        self.start_freq_entry.bind("<FocusOut>", self.freq_limits_check)

    def inc_opt_counter(self):
        self.opt_counter = self.opt_counter + 1
    
    def last_opt_added(self):
        self.opt_counter = self.opt_counter + 0.5

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

    
    
