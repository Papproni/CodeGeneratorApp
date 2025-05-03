import tkinter as tk
from tkinter import Canvas, Menu, StringVar, OptionMenu
from gui_blocks.gui_elements.option_manager import OptionManager

math_color = "orange"
max_input_lim = 16

class AddBlock(OptionManager):
    def __init__(self,canvas :Canvas,tag,x=None,y=None,load_data = None):
        super().__init__()
        self.canvas = canvas

        # default values
        self.type            = "add_block"
        # must be changed 
        self.tag             = tag
        
        # NO INPUT DEFINED
        self.input_num       = 2
        self.input_channel   = 2

        # ONE OUTPUT DEFINED
        self.output_num      = 1
        self.output_channel  = 1

        # Create Block
        if x is None:
            self.x = 50
            self.y = 50
        else:
            self.x = x
            self.y = y

        self.circle_y_offset    = 5  # px
        self.circle_y_distance  = 25 # px
        self.io_circle_radius   = 10 # px

        self.w = 40 # px
        self.num_of_inputs = 2
        self.h = self.circle_y_offset + self.num_of_inputs * self.circle_y_distance
        
        # Option params
        self.opt_start_y    = 20
        self.opt_height     = 75 # pixel
        self.opt_counter    = 0
        self.opt_text_start = 20 # 20%
        self.opt_box_start  = 70 # 70%
        
        self.bg  = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+self.h, fill=math_color,         tags=("block", self.tag,"text_background"))
        self.text     = self.canvas.create_text(     self.x+self.w/2,    self.y+self.h/2, text="+", font=("Arial", 14), tags=("block", self.tag) )
        

        self.input_circle_y =self.y+self.circle_y_offset 
        self.input_circles = []
        for i in range(self.num_of_inputs):
            self.input_circles.append(self.canvas.create_oval(self.x-self.io_circle_radius,     self.input_circle_y, self.x+10, self.y+25+25*i, fill="green",              tags=("input_circle", self.tag)))
            self.input_circle_y = self.input_circle_y + self.circle_y_distance
        
        # self.input_circle2       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.input_circle_y, self.x+10, self.y+50, fill="green",              tags=("input_circle", self.tag))
        # self.input_circle_y = self.input_circle_y + self.circle_y_distance
        # self.input_circle3       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.input_circle_y, self.x+10, self.y+75, fill="green",              tags=("input_circle", self.tag))
        
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+(self.h/2-self.io_circle_radius), self.x+self.w+10, self.y+(self.h/2+self.io_circle_radius), fill="yellow",            tags=("output_circle", self.tag))

        # OPTIONS: 
        self.add_option("INPUT_NUM",  "NUM", self.num_of_inputs, max_input_lim,default_value=2, visible_on_block=False,callback_on_value_change=self.changing_size_of_block)
        self.last_opt_added()
        canvas.tag_lower("background",'all')
    
    def changing_size_of_block(self,num_of_inputs):
        self.num_of_inputs = num_of_inputs
        self.h = self.circle_y_offset + self.num_of_inputs * self.circle_y_distance

        for circle in self.input_circles:
            self.canvas.delete(circle)
        self.x,self.y,x2,y2 = self.canvas.coords(self.tag)
        
        # update old block data
        self.canvas.coords(self.bg,self.x,  self.y, self.x+self.w, self.y+self.h)
        self.canvas.coords(self.text,self.x+self.w/2,    self.y+self.h/2)
        self.canvas.coords(self.output_circle,self.x+self.w-self.io_circle_radius,   self.y+(self.h/2-self.io_circle_radius), self.x+self.w+10, self.y+(self.h/2+self.io_circle_radius))
        
        self.input_circle_y =self.y+self.circle_y_offset 
        self.input_circles = []
        for i in range(self.num_of_inputs):
            self.input_circles.append(self.canvas.create_oval(self.x-self.io_circle_radius,     self.input_circle_y, self.x+10, self.y+25+25*i, fill="green",              tags=("input_circle", self.tag)))
            self.canvas.delete()
            self.input_circle_y = self.input_circle_y + self.circle_y_distance
        
        print("changin_size_of_block")

class SubBlock(OptionManager):
    def __init__(self,canvas,tag,x=None,y=None,load_data = None):
        super().__init__()
        self.canvas = canvas

        # default values
        self.type            = "sub_block"
        # must be changed 
        self.tag             = tag
        
        # NO INPUT DEFINED
        self.input_num       = 2
        self.input_channel   = 2

        # ONE OUTPUT DEFINED
        self.output_num      = 1
        self.output_channel  = 1

         # Create Block
        if x is None:
            self.x = 50
            self.y = 50
        else:
            self.x = x
            self.y = y
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
        self.add_option("INPUT_NUM",  "NUM", 2, max_input_lim,default_value=2, visible_on_block=False,bindable=False)
        self.last_opt_added()
        canvas.tag_lower("background",'all')
        
class DivBlock(OptionManager):
    def __init__(self,canvas,tag,x=None,y=None, load_data = None):
        super().__init__()
        self.canvas = canvas

        # default values
        self.type            = "div_block"
        # must be changed 
        self.tag             = tag
        
        # NO INPUT DEFINED
        self.input_num       = 2
        self.input_channel   = 2

        # ONE OUTPUT DEFINED
        self.output_num      = 1
        self.output_channel  = 1

         # Create Block
        if x is None:
            self.x = 50
            self.y = 50
        else:
            self.x = x
            self.y = y
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
        self.add_option("INPUT_NUM",  "NUM", 2, max_input_lim,default_value=2, visible_on_block=False,bindable=False)
        self.last_opt_added()
        canvas.tag_lower("background",'all')

class MulBlock(OptionManager):
    def __init__(self,canvas,tag,x = None,y = None, load_data = None):
        super().__init__()
        self.canvas = canvas

        # default values
        self.type            = "mul_block"
        # must be changed 
        self.tag             = tag
        
        # NO INPUT DEFINED
        self.input_num       = 2
        self.input_channel   = 2

        # ONE OUTPUT DEFINED
        self.output_num      = 1
        self.output_channel  = 1

         # Create Block
        if x is None:
            self.x = 50
            self.y = 50
        else:
            self.x = x
            self.y = y
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
        self.add_option("INPUT_NUM",  "NUM", 2, max_input_lim,default_value=2, visible_on_block=False, bindable=False)
        self.last_opt_added()
        canvas.tag_lower("background",'all')
class ABSBlock(OptionManager):
    def __init__(self,canvas,tag,x = None,y = None, load_data = None):
        super().__init__()
        self.canvas = canvas

        # default values
        self.type            = "abs_block"
        # must be changed 
        self.tag             = tag
        
        # NO INPUT DEFINED
        self.input_num       = 1
        self.input_channel   = 1

        # ONE OUTPUT DEFINED
        self.output_num      = 1
        self.output_channel  = 1

        # Create Block
        if x is None:
            self.x = 50
            self.y = 50
        else:
            self.x = x
            self.y = y

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
    def __init__(self,canvas,tag,x = None,y = None, load_data = None):
        
        super().__init__()
        
        self.canvas = canvas

        # default values
        self.type            = "lim_block"
        # must be changed 
        self.tag             = tag
        
        # NO INPUT DEFINED
        self.input_num       = 1
        self.input_channel   = 1

        # ONE OUTPUT DEFINED
        self.output_num      = 1
        self.output_channel  = 1

         # Create Block
        if x is None:
            self.x = 50
            self.y = 50
        else:
            self.x = x
            self.y = y
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
    def __init__(self,canvas,tag,x = None,y = None, load_data = None):
        super().__init__()
        self.canvas = canvas

        # default values
        self.type            = "const_block"
        # must be changed 
        self.tag             = tag
        
        # NO INPUT DEFINED
        self.input_num       = 0
        self.input_channel   = 0

        # ONE OUTPUT DEFINED
        self.output_num      = 1
        self.output_channel  = 1

         # Create Block
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
        
