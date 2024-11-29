import tkinter as tk
from tkinter import Canvas, Menu, StringVar, OptionMenu
from gui_blocks.gui_elements.option_manager import OptionManager
# No parameter needed
# init:
# type: input
# Source: 
# numofInputs: 0
# number of channels per inputs: 0
# numofOutputs: 1
# number of channels per outputs: 1


class InputBlock:
    def __init__(self,canvas,tag,x=None,y=None,load_data = None):
        # default values
        self.type            = "input_block"
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
    def __init__(self,canvas,tag,x=None,y=None,load_data = None):
        super().__init__()
        # default values
        self.type            = "output_block"
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

class GeneratorBlock(OptionManager):
    def __init__(self,canvas,tag,x = None,y = None, load_data = None):
        super().__init__()
        self.canvas = canvas
        self.type            = "generator_block"
        self.tag             = tag
        # NO INPUT DEFINED
        self.input_num       = 0
        self.input_channel   = 0
        # ONE OUTPUT DEFINED
        self.output_num      = 1
        self.output_channel  = 1
        if x is None:
            self.x = 50
            self.y = 50
        else:
            self.x = x
            self.y = y
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
        self.filterbank_text     = self.canvas.create_text(     self.x+self.w/2,    self.y+20, text="Generator", font=("Arial", 14), tags=("block", self.tag) )
        
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+15, self.x+self.w+10, self.y+35, fill="yellow",            tags=("output_circle", self.tag))
        
        # OPTIONS:
        #   Freq:           
        #   Amp:            
        #   Sig:            
        #   Offset:            
        self.add_option("Freq","NUM",1,20000,default_value=10)
        self.add_option("Amp","NUM",0,65535,default_value=1)
        self.add_option("Sig","OPTIONBOX",default_value="SINE,TRIANGLE,SQUARE",bindable=False)
        self.add_option("Offs","NUM",0,65535,default_value=10)
        
        self.last_opt_added()
        self.filterbank_block    = self.canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.opt_start_y+self.opt_height*self.opt_counter, fill="red",         tags=("block", self.tag,"background"))
        canvas.tag_lower("background",'all')
    
