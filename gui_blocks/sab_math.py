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

class ABSBlock:
    def __init__(self,canvas,tag):
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
        self.filterbank_text_bg  = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+self.h, fill=math_color,         tags=("block", self.tag,"text_background"))
        self.filterbank_text     = self.canvas.create_text(     self.x+self.w/2,    self.y+self.h/2, text="ABS", font=("Arial", 14), tags=("block", self.tag) )
        
        self.input_circle        = self.canvas.create_oval(self.x-self.io_circle_radius,   self.y+(self.h/2-self.io_circle_radius), self.x+10, self.y+(self.h/2+self.io_circle_radius), fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+(self.h/2-self.io_circle_radius), self.x+self.w+10, self.y+(self.h/2+self.io_circle_radius), fill="yellow",            tags=("output_circle", self.tag))
        
    
class LimitBlock:
    def __init__(self,canvas,tag):
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
        self.w = 100
        self.io_circle_radius = 10
        
        # Option params
        self.opt_start_y    = 20
        self.opt_height     = 40 # pixel
        self.opt_counter    = 0
        self.opt_text_start = 20 # 20%
        self.opt_box_start  = 70 # 70%
        
        
        # self.filterbank_block    = canvas.create_rectangle(x, y, x+100, y+75+option_height*3, fill="red",         tags=("block", tag,"background"))
        self.title_text_bg  = self.canvas.create_rectangle(self.x,  self.y, self.x+self.w, self.y+40, fill=math_color,         tags=("block", self.tag,"text_background"))
        self.title_text     = self.canvas.create_text(     self.x+self.w/2,    self.y+20, text="Limit", font=("Arial", 14), tags=("block", self.tag) )
        
        self.input_circle        = self.canvas.create_oval(self.x-self.io_circle_radius,     self.y+15, self.x+10, self.y+35, fill="green",              tags=("input_circle", self.tag))
        self.output_circle       = self.canvas.create_oval(self.x+self.w-self.io_circle_radius,   self.y+15, self.x+self.w+10, self.y+35, fill="yellow",            tags=("output_circle", self.tag))
        
        
        self.option_vars = {}
        
        # OPTIONS:
        #   LimLow:    
        #   LimHigh:    
        self.add_option("LOW", "NUM", -20000, 20000)
        self.add_option("HIGH", "NUM", -20000, 20000)
        # self.add_option("low_lim","NUM",-20000,20000)
        # self.add_option("type","MENU",("FIRST","SECOND","THIRD"))
        self.last_opt_added()
        self.filterbank_block    = self.canvas.create_rectangle(self.x, self.y, self.x+self.w, self.y+self.opt_start_y+self.opt_height*self.opt_counter, 
                                                                fill="red",tags=("block", self.tag,"background"))
        canvas.tag_lower("background",'all')

    def add_option(self, option_name, option_type, min_value=None, max_value=None, default_value="1"):
        self.inc_opt_counter()

        # Create a StringVar to hold the value of the option
        var = tk.StringVar(value=default_value)
        self.option_vars[option_name] = var

        # Create the entry widget, bind it to the StringVar
        entry = tk.Entry(self.canvas, width=5, textvariable=var)

        # Display the option name on the canvas
        text = option_name.capitalize()
        self.canvas.create_text(
            self.x + 0.2 * self.w,
            self.y + self.opt_start_y + self.opt_height * self.opt_counter,
            text=text,
            font=("Arial", 14),
            tags=("block", self.tag)
        )

        # Create window for the entry widget in the canvas
        self.canvas.create_window(
            self.x + 0.7 * self.w,
            self.y + self.opt_start_y + self.opt_height * self.opt_counter,
            window=entry,
            tags=(f"{option_name}_entry", self.tag),
            anchor="center"
        )

        # Bind the validation based on the option type
        if option_type == "NUM":
            entry.bind("<FocusOut>", lambda event, e=entry: self.validate_numeric_input(e, var, min_value, max_value, default_value))

    def validate_numeric_input(self, entry, var, min_value, max_value, default_value):
        value = var.get()
        try:
            num = int(value)
            if min_value is not None and num < min_value:
                raise ValueError("Value is below the minimum limit")
            if max_value is not None and num > max_value:
                raise ValueError("Value is above the maximum limit")
        except ValueError:
            var.set(default_value)  # Reset to default if invalid
            entry.delete(0, tk.END)
            entry.insert(0, default_value)
    
    def inc_opt_counter(self):
        self.opt_counter = self.opt_counter + 1
    
    def last_opt_added(self):
        self.opt_counter = self.opt_counter + 0.5
