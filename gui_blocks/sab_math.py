import tkinter as tk
from tkinter import Canvas, Menu, StringVar, OptionMenu
from gui_blocks.gui_elements.option_manager import OptionManager

math_color = "orange"
max_input_lim = 2

class AddBlock(OptionManager):
    def __init__(self,canvas,tag):
        super().__init__()
        self.canvas = canvas

        # default values
        self.type            = "ADD_BLOCK"
        # must be changed 
        self.tag             = tag
        
        # NO INPUT DEFINED
        self.input_num       = 2
        self.input_channel   = 2

        # ONE OUTPUT DEFINED
        self.output_num      = 1
        self.output_channel  = 1

        # Create Block
        self.x = 50
        self.y = 50
        self.w = 40
        self.h = 55
        self.io_circle_radius = 10
        
        # Option params
        self.opt_start_y    = 20
        self.opt_height     = 50 # pixel
        self.opt_counter    = 0
        self.opt_text_start = 20 # 20%
        self.opt_box_start  = 70 # 70%
        
        
        # self.filterbank_block    = canvas.create_rectangle(x, y, x+100, y+75+option_height*3, fill="red",         tags=("block", tag,"background"))
        self.bg  = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+self.h, fill=math_color,         tags=("block", self.tag,"text_background"))
        self.text     = self.canvas.create_text(     self.x+self.w/2,    self.y+self.h/2, text="+", font=("Arial", 14), tags=("block", self.tag) )
        
        self.input_circle1       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+5, self.x+10, self.y+25, fill="green",              tags=("input_circle", self.tag))
        self.input_circle2       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+30, self.x+10, self.y+50, fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+(self.h/2-self.io_circle_radius), self.x+self.w+10, self.y+(self.h/2+self.io_circle_radius), fill="yellow",            tags=("output_circle", self.tag))

        # OPTIONS: 
        self.add_option("INPUT NUM",  "NUM", 2, max_input_lim,default_value=2, visible_on_block=False,bindable=False)
        self.last_opt_added()
        canvas.tag_lower("background",'all')
class SubBlock(OptionManager):
    def __init__(self,canvas,tag):
        super().__init__()
        self.canvas = canvas

        # default values
        self.type            = "SUB_BLOCK"
        # must be changed 
        self.tag             = tag
        
        # NO INPUT DEFINED
        self.input_num       = 2
        self.input_channel   = 2

        # ONE OUTPUT DEFINED
        self.output_num      = 1
        self.output_channel  = 1

        # Create Block
        self.x = 50
        self.y = 50
        self.w = 40
        self.h = 55
        self.io_circle_radius = 10
        
        # Option params
        self.opt_start_y    = 20
        self.opt_height     = 50 # pixel
        self.opt_counter    = 0
        self.opt_text_start = 20 # 20%
        self.opt_box_start  = 70 # 70%
        
        
        # self.filterbank_block    = canvas.create_rectangle(x, y, x+100, y+75+option_height*3, fill="red",         tags=("block", tag,"background"))
        self.bg    = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+self.h, fill=math_color,         tags=("block", self.tag,"text_background"))
        self.text  = self.canvas.create_text(     self.x+self.w/2,    self.y+self.h/2, text="-", font=("Arial", 20), tags=("block", self.tag) )
        
        self.input_circle1       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+5, self.x+10, self.y+25, fill="green",              tags=("input_circle", self.tag))
        self.input_circle2       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+30, self.x+10, self.y+50, fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+(self.h/2-self.io_circle_radius), self.x+self.w+10, self.y+(self.h/2+self.io_circle_radius), fill="yellow",            tags=("output_circle", self.tag))

                # OPTIONS: 
        self.add_option("INPUT NUM",  "NUM", 2, max_input_lim,default_value=2, visible_on_block=False,bindable=False)
        self.last_opt_added()
        canvas.tag_lower("background",'all')
        
class DivBlock(OptionManager):
    def __init__(self,canvas,tag):
        super().__init__()
        self.canvas = canvas

        # default values
        self.type            = "DIV_BLOCK"
        # must be changed 
        self.tag             = tag
        
        # NO INPUT DEFINED
        self.input_num       = 2
        self.input_channel   = 2

        # ONE OUTPUT DEFINED
        self.output_num      = 1
        self.output_channel  = 1

        # Create Block
        self.x = 50
        self.y = 50
        self.w = 40
        self.h = 55
        self.io_circle_radius = 10
        
        # Option params
        self.opt_start_y    = 20
        self.opt_height     = 50 # pixel
        self.opt_counter    = 0
        self.opt_text_start = 20 # 20%
        self.opt_box_start  = 70 # 70%
        
        
        # self.filterbank_block    = canvas.create_rectangle(x, y, x+100, y+75+option_height*3, fill="red",         tags=("block", tag,"background"))
        self.bg    = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+self.h, fill=math_color,         tags=("block", self.tag,"text_background"))
        self.text  = self.canvas.create_text(     self.x+self.w/2,    self.y+self.h/2, text="÷", font=("Arial", 18), tags=("block", self.tag) )
        
        self.input_circle1       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+5, self.x+10, self.y+25, fill="green",              tags=("input_circle", self.tag))
        self.input_circle2       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+30, self.x+10, self.y+50, fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+(self.h/2-self.io_circle_radius), self.x+self.w+10, self.y+(self.h/2+self.io_circle_radius), fill="yellow",            tags=("output_circle", self.tag))
        # OPTIONS: 
        self.add_option("INPUT NUM",  "NUM", 2, max_input_lim,default_value=2, visible_on_block=False,bindable=False)
        self.last_opt_added()
        canvas.tag_lower("background",'all')

class MulBlock(OptionManager):
    def __init__(self,canvas,tag):
        super().__init__()
        self.canvas = canvas

        # default values
        self.type            = "MUL_BLOCK"
        # must be changed 
        self.tag             = tag
        
        # NO INPUT DEFINED
        self.input_num       = 2
        self.input_channel   = 2

        # ONE OUTPUT DEFINED
        self.output_num      = 1
        self.output_channel  = 1

        # Create Block
        self.x = 50
        self.y = 50
        self.w = 40
        self.h = 55
        self.io_circle_radius = 10
        
        # Option params
        self.opt_start_y    = 20
        self.opt_height     = 50 # pixel
        self.opt_counter    = 0
        self.opt_text_start = 20 # 20%
        self.opt_box_start  = 70 # 70%
        
        
        # self.filterbank_block    = canvas.create_rectangle(x, y, x+100, y+75+option_height*3, fill="red",         tags=("block", tag,"background"))
        self.bg    = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+self.h, fill=math_color,         tags=("block", self.tag,"text_background"))
        self.text  = self.canvas.create_text(     self.x+self.w/2,    self.y+self.h/2, text="X", font=("Arial", 14), tags=("block", self.tag) )
        
        self.input_circle1       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+5, self.x+10, self.y+25, fill="green",              tags=("input_circle", self.tag))
        self.input_circle2       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+30, self.x+10, self.y+50, fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+(self.h/2-self.io_circle_radius), self.x+self.w+10, self.y+(self.h/2+self.io_circle_radius), fill="yellow",            tags=("output_circle", self.tag))
        # OPTIONS: 
        self.add_option("INPUT NUM",  "NUM", 2, max_input_lim,default_value=2, visible_on_block=False, bindable=False)
        self.last_opt_added()
        canvas.tag_lower("background",'all')
class ABSBlock(OptionManager):
    def __init__(self,canvas,tag):
        super().__init__()
        self.canvas = canvas

        # default values
        self.type            = "ABS_BLOCK"
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
        self.w = 60
        self.h = 30
        self.io_circle_radius = 10
        
        # Option params
        self.opt_start_y    = 20
        self.opt_height     = 50 # pixel
        self.opt_counter    = 0
        self.opt_text_start = 20 # 20%
        self.opt_box_start  = 70 # 70%
        
        
        # self.filterbank_block    = canvas.create_rectangle(x, y, x+100, y+75+option_height*3, fill="red",         tags=("block", tag,"background"))
        self.bg    = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+self.h, fill=math_color,         tags=("block", self.tag,"text_background"))
        self.text  = self.canvas.create_text(     self.x+self.w/2,    self.y+self.h/2, text="ABS", font=("Arial", 14), tags=("block", self.tag) )
        
        self.input_circle        = self.canvas.create_oval(self.x-self.io_circle_radius,   self.y+(self.h/2-self.io_circle_radius), self.x+10, self.y+(self.h/2+self.io_circle_radius), fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+(self.h/2-self.io_circle_radius), self.x+self.w+10, self.y+(self.h/2+self.io_circle_radius), fill="yellow",            tags=("output_circle", self.tag))
        

class LimitBlock(OptionManager):
    def __init__(self,canvas,tag):
        
        super().__init__()
        
        self.canvas = canvas

        # default values
        self.type            = "LIM_BLOCK"
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
        self.w = 120
        self.io_circle_radius = 10
        
        # Option params
        self.opt_start_y    = 20
        self.opt_height     = 40 # pixel
        self.opt_counter    = 0
        self.opt_text_start = 20 # 20%
        self.opt_box_start  = 70 # 70%
        
        
        # self.filterbank_block    = canvas.create_rectangle(x, y, x+100, y+75+option_height*3, fill="red",         tags=("block", tag,"background"))
        self.bg   = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+40, fill=math_color,         tags=("block", self.tag,"text_background"))
        self.text = self.canvas.create_text(     self.x+self.w/2,    self.y+20, text="Limit", font=("Arial", 14), tags=("block", self.tag) )
        
        self.input_circle        = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+15, self.x+10, self.y+35, fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+15, self.x+self.w+10, self.y+35, fill="yellow",            tags=("output_circle", self.tag))
        
        
        # 
        
        # OPTIONS:
        #   LimLow:    
        #   LimHigh:    
        self.add_option("LOW",  "NUM", -20000, 20000,bindable=True)
        self.add_option("HIGH", "NUM", -20000, 20000,bindable=True)
        # self.option_vars

        # self.add_option("low_lim","NUM",-20000,20000)
        # self.add_option("type","MENU",("FIRST","SECOND","THIRD"))
        self.last_opt_added()
        self.filterbank_block    = self.canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.opt_start_y+self.opt_height*self.opt_counter, 
                                                                fill="red",tags=("block", self.tag,"background"))
        canvas.tag_lower("background",'all')
    
    

class ConstBlock(OptionManager):
    def __init__(self,canvas,tag):
        super().__init__()
        self.canvas = canvas

        # default values
        self.type            = "CONST_BLOCK"
        # must be changed 
        self.tag             = tag
        
        # NO INPUT DEFINED
        self.input_num       = 0
        self.input_channel   = 0

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
        
        self.title_text_bg  = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+40, fill="grey",         tags=("block", self.tag,"text_background"))
        self.title_text     = self.canvas.create_text(     self.x+self.w/2,    self.y+20, text="Const", font=("Arial", 14), tags=("block", self.tag) )
        # OPTIONS: 
        self.add_option("VALUE",  "NUM", -32768, 32768,default_value=1)
        self.add_option("Type","OPTIONBOX",default_value="INT,FLOAT", visible_on_block=False, bindable=False)
        self.last_opt_added()

        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+15, self.x+self.w+10, self.y+35, fill="yellow",            tags=("output_circle", self.tag))

        self.filterbank_block    = self.canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.opt_start_y+self.opt_height*self.opt_counter, 
                                                                fill="red",tags=("block", self.tag,"background"))
        canvas.tag_lower("background",'all')
        
