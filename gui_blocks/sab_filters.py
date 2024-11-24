import tkinter as tk
from tkinter import Canvas, Menu, StringVar, OptionMenu
from gui_blocks.gui_elements.option_manager import OptionManager
import numpy as np
# FILTERBANK BLOCK------------------------------------------------------
# init:
# type: Filter
# Source: 
# numofInputs: 1
# number of channels per inputs: 1
# numofOutputs: 1
# number of channels per inputs: USER DEFINED
class FilterBank(OptionManager):
    def __init__(self,canvas,tag):
        super().__init__()
        
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
        self.add_option("Bins","NUM",1,100,default_value=44)
        self.add_option("Q","NUM",0.0,2.0,default_value=0.707)
        self.add_option("Step","OPTIONBOX",default_value="LIN,LOG",bindable=False)
        
        self.last_opt_added()
        self.filterbank_block    = self.canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.opt_start_y+self.opt_height*self.opt_counter, fill="red",         tags=("block", self.tag,"background"))
        canvas.tag_lower("background",'all')
    
    
    
#   ------------------------------------------------------

# BIQUAD BLOCK------------------------------------------------------
# init:
# type: Filter
# Source: 
# numofInputs:                      1
# number of channels per inputs:    1
# numofOutputs:                     1
# number of channels per inputs:    1
class BiquadFilter(OptionManager):
    def __init__(self,canvas,tag):
        super().__init__()
        
        
        self.canvas = canvas

        # default values
        self.type            = "BIQUAD_FILTER"
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
        self.title_text_bg  = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+40, fill="grey",         tags=("block", self.tag,"text_background"))
        self.title_text     = self.canvas.create_text(     self.x+self.w/2,    self.y+20, text="Biquad Filter", font=("Arial", 14), tags=("block", self.tag) )
        
        self.input_circle        = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+15, self.x+10, self.y+35, fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+15, self.x+self.w+10, self.y+35, fill="yellow",            tags=("output_circle", self.tag))
        
        # OPTIONS:
        #   freq:           cutoff Frequency
        #   Q:              Filter characteristics  
        #   Type:           Type of filter           
        self.add_option("Type","OPTIONBOX",default_value="LPF,HPF,BANDPASS,NOTCH",bindable=False)
        self.add_option("Freq","NUM",10,20000,default_value=440)
        self.add_option("Q","NUM",0.1,100,default_value=0.707)
        self.add_option("Gain","NUM",0,10,default_value=1)
        
        self.last_opt_added()
        self.filterbank_block    = self.canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.opt_start_y+self.opt_height*self.opt_counter, 
                                                                fill="red",tags=("block", self.tag,"background"))
        canvas.tag_lower("background",'all')

    def fill_template_data(self,template_data):
        sample_rate = 48000
        
        Type    = self.option_vars['Type'].get('var').get()
        Freq    = float(self.option_vars['Freq'].get('var').get())
        Q       = float(self.option_vars['Q'].get('var').get())

        omega = 2 * np.pi * Freq / sample_rate
        cos_omega = np.cos(omega)
        alpha = np.sin(omega) / (2 * Q)
        
        b1 = b2 = a0 = a1 = a2 = 0
    
        if Type == 'LPF':
            a0 = (1 + alpha)
            b1 = (1 - cos_omega)
            b2 = (1 - cos_omega)
            a1 = -2 * cos_omega / a0
            a2 = (1 - alpha) / a0
        
        elif Type == 'HPF':
            a0 = (1 + alpha)
            b1 = -(1 + cos_omega)
            b2 = (1 + cos_omega)
            a1 = -2 * cos_omega / a0
            a2 = (1 - alpha) / a0
        
        elif Type == 'NOTCH':
            a0 = (1 + alpha)
            b1 = -2 * cos_omega
            b2 = 1
            a1 = -2 * cos_omega / a0
            a2 = (1 - alpha) / a0
        
        elif Type == 'BANDPASS':
            a0 = (1 + alpha)
            b1 = 0
            b2 = -Q * alpha
            a1 = -2 * cos_omega / a0
            a2 = (1 - alpha) / a0
        
        template_data["b0"] = a0
        template_data["b1"] = a1
        template_data["b2"] = a2
        template_data["a1"] = b1
        template_data["a2"] = b2
#   ------------------------------------------------------

# BIQUAD BLOCK------------------------------------------------------
# init:
# type: Filter
# Source: 
# numofInputs:                      1
# number of channels per inputs:    1
# numofOutputs:                     1
# number of channels per inputs:    1
class MovingAverage(OptionManager):
    def __init__(self,canvas,tag):
        super().__init__()
        self.canvas = canvas

        # default values
        self.type            = "MOVING_AVG_FILTER"
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
        self.w = 150
        self.io_circle_radius = 10
        
        # Option params
        self.opt_start_y    = 20
        self.opt_height     = 50 # pixel
        self.opt_counter    = 0
        self.opt_text_start = 20 # 20%
        self.opt_box_start  = 70 # 70%
        
        
        # self.filterbank_block    = canvas.create_rectangle(x, y, x+100, y+75+option_height*3, fill="red",         tags=("block", tag,"background"))
        self.title_text_bg  = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+40, fill="grey",         tags=("block", self.tag,"text_background"))
        self.title_text     = self.canvas.create_text(     self.x+self.w/2,    self.y+20, text="MAVG Filter", font=("Arial", 14), tags=("block", self.tag) )
        
        self.input_circle        = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+15, self.x+10, self.y+35, fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+15, self.x+self.w+10, self.y+35, fill="yellow",            tags=("output_circle", self.tag))
        
        # OPTIONS:
        #   buffer size:           cutoff Frequency   
        self.add_option("BuffSize","NUM",2,96000,default_value=10,bindable=False)        
     
        self.last_opt_added()
        self.filterbank_block    = self.canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.opt_start_y+self.opt_height*self.opt_counter, 
                                                                fill="red",tags=("block", self.tag,"background"))
        canvas.tag_lower("background",'all')
#   ------------------------------------------------------
    
