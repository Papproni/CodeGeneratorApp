import tkinter as tk
from tkinter import Canvas, Menu, StringVar, OptionMenu


math_color = "orange"

class AddBlock:
    def __init__(self,canvas,tag):
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
        self.filterbank_text_bg  = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+self.h, fill=math_color,         tags=("block", self.tag,"text_background"))
        self.filterbank_text     = self.canvas.create_text(     self.x+self.w/2,    self.y+self.h/2, text="+", font=("Arial", 14), tags=("block", self.tag) )
        
        self.input_circle1       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+5, self.x+10, self.y+25, fill="green",              tags=("input_circle", self.tag))
        self.input_circle2       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+30, self.x+10, self.y+50, fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+(self.h/2-self.io_circle_radius), self.x+self.w+10, self.y+(self.h/2+self.io_circle_radius), fill="yellow",            tags=("output_circle", self.tag))
class SubBlock:
    def __init__(self,canvas,tag):
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
        self.filterbank_text_bg  = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+self.h, fill=math_color,         tags=("block", self.tag,"text_background"))
        self.filterbank_text     = self.canvas.create_text(     self.x+self.w/2,    self.y+self.h/2, text="-", font=("Arial", 20), tags=("block", self.tag) )
        
        self.input_circle1       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+5, self.x+10, self.y+25, fill="green",              tags=("input_circle", self.tag))
        self.input_circle2       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+30, self.x+10, self.y+50, fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+(self.h/2-self.io_circle_radius), self.x+self.w+10, self.y+(self.h/2+self.io_circle_radius), fill="yellow",            tags=("output_circle", self.tag))
        
class DivBlock:
    def __init__(self,canvas,tag):
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
        self.filterbank_text_bg  = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+self.h, fill=math_color,         tags=("block", self.tag,"text_background"))
        self.filterbank_text     = self.canvas.create_text(     self.x+self.w/2,    self.y+self.h/2, text="÷", font=("Arial", 18), tags=("block", self.tag) )
        
        self.input_circle1       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+5, self.x+10, self.y+25, fill="green",              tags=("input_circle", self.tag))
        self.input_circle2       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+30, self.x+10, self.y+50, fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+(self.h/2-self.io_circle_radius), self.x+self.w+10, self.y+(self.h/2+self.io_circle_radius), fill="yellow",            tags=("output_circle", self.tag))
        
class MulBlock:
    def __init__(self,canvas,tag):
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
        self.filterbank_text_bg  = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+self.h, fill=math_color,         tags=("block", self.tag,"text_background"))
        self.filterbank_text     = self.canvas.create_text(     self.x+self.w/2,    self.y+self.h/2, text="X", font=("Arial", 14), tags=("block", self.tag) )
        
        self.input_circle1       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+5, self.x+10, self.y+25, fill="green",              tags=("input_circle", self.tag))
        self.input_circle2       = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+30, self.x+10, self.y+50, fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+(self.h/2-self.io_circle_radius), self.x+self.w+10, self.y+(self.h/2+self.io_circle_radius), fill="yellow",            tags=("output_circle", self.tag))
        

