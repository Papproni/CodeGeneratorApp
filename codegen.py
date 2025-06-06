import tkinter as tk
from tkinter import Canvas, Menu, StringVar, OptionMenu,filedialog

# BLOCKS
# import sab_filters
# import sab_io
from gui_blocks import sab_filters
from gui_blocks import sab_io
from gui_blocks import sab_math

import fx_builder

import slidemenu
import SAB_save

import networkx as nx
import xml.etree.ElementTree as ET

class Potmeter:
    def __init__(self):
        self.name = "None"
        self.lim_low = 0
        self.lim_high = 10

class HardwareControls:
    def __init__(self):
        self.pots = Potmeter()
        self.slots = []
        self.max_slot_num = 12
    
    def assign_control(self,slot_location):
        self.slots.append

class CodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Code Generator for SAB_V3")
        root.geometry("1000x1000")

        self.codegen_location_src = None
        self.codegen_location_inc = None

        self.canvas = Canvas(root, width=800, height=800, bg="white")
        self.canvas.pack()

        self.slidemenu = slidemenu.SlideMenu(root,self.generate_c_code)
        self.blocks = []
        self.arrows = []

        self.save_load      = SAB_save.SAB_save_load(self.canvas,
                                                self.blocks,
                                                self.arrows,
                                                self.slidemenu.fx_parameters)
        self.selected_output_circle = None
        self.arrow_line = None
        self.drag_data = {"x": 0, "y": 0, "item": None, "tags": None}

        self.unique_num = 0

        self.create_menu()
        self.bind_events()
        self.root.bind("<Escape>", self.cancel_arrow)

        # Create the right-click context menu
        self.context_menu = Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Delete Block", command=self.delete_block)
        self.context_menu.add_command(label="Delete Arrow", command=self.delete_arrow)
        self.context_menu.add_command(label="Reset Controls", command=self.reset_controls)



    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_checkbutton(label="WindowTopLock", command=self.top_lock_window)
        file_menu.add_command(label="Save", command=self.save_custom_fx)
        file_menu.add_command(label="Load", command=self.load_custom_fx)
        file_menu.add_command(label="Choose gen loc", command=self.set_gen_location)

        
        io_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="IO", menu=io_menu)

        io_menu.add_command(label="Input", command=self.add_input_block)
        io_menu.add_command(label="Output", command=self.add_output_block)
        io_menu.add_command(label="Generator", command=self.add_generator_block)

        filter_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Filters", menu=filter_menu)
        filter_menu.add_command(label="Filterbank", command=self.add_filterbank_block)
        filter_menu.add_command(label="Biquad",     command=self.add_biquad_filter_block)
        filter_menu.add_command(label="Moving Avg", command=self.add_mavg_filter_block)


        math_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Math", menu=math_menu)
        
        math_menu.add_command(label="Const",    command=self.add_const_block)
        math_menu.add_command(label="Add",      command=self.add_add_block)
        math_menu.add_command(label="Mul",      command=self.add_mul_block)
        math_menu.add_command(label="Div",      command=self.add_div_block)
        math_menu.add_command(label="Sub",      command=self.add_sub_block)
        math_menu.add_command(label="Lim",      command=self.add_lim_block)
        math_menu.add_command(label="ABS",      command=self.add_abs_block)
        
        special_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Special", menu=special_menu)
        
        special_menu.add_command(label="Generator",     command=self.add_add_block)
        special_menu.add_command(label="Delay line",    command=self.add_add_block)
        special_menu.add_command(label="Reverb",        command=self.add_add_block)
        special_menu.add_command(label="PitchShift",    command=self.add_add_block)
        
        special_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Control", menu=special_menu)
        
        special_menu.add_command(label="PID",                       command=self.add_add_block)
        special_menu.add_command(label="State Space Control",       command=self.add_add_block)

    def top_lock_window(self):
        print("top_lock_window")
        current = bool(self.root.wm_attributes("-topmost"))
        self.root.wm_attributes("-topmost", not current)

    def save_custom_fx(self):
        print("SAVE")
        self.save_load.save()
    
    def call_function_with_params(self, block_type, **kwargs):
        func_name = f"add_{block_type}"  # Construct the function name dynamically
        func = getattr(self, func_name, None)  # Get the function by name
        if callable(func):
            func(**kwargs)  # Call the function with the provided keyword arguments
        else:
            print(f"Function {func_name} does not exist!")
            
    def load_custom_fx(self):
        # Delete all elements, settings
        for block in self.blocks[:]:
            self.delete_block(block.tag)

        blocks,arrows, fx_params, block_options,fx_params_options = self.save_load.load()
        # Init blocks
        for block in blocks:
            x = int(float(block.attrib['x']))
            y = int(float(block.attrib['y']))
            self.call_function_with_params(block.attrib['type'],
                                           tag = block.attrib['tag'],
                                           x = x,
                                           y = y
                                           )
            try:
                for block_option in block_options[block.attrib['tag']].attrib:
                    value = block_options[block.attrib['tag']].attrib[block_option]
                    if "param" in value:
                        self.blocks[-1].option_vars[block_option]['binded_src'] = value
                    self.blocks[-1].option_vars[block_option]['var'].set(value)

            except:
                pass
            
        # init arrows

        input_circle_items = self.canvas.find_withtag("input_circle")
        output_circle_items = self.canvas.find_withtag("output_circle")
        self.canvas.find_withtag('block4')
        input_ID = None
        output_ID = None
        for arrow in arrows:
            src_tag = arrow.attrib["src_block_tag"]
            dst_tag = arrow.attrib["dst_block_tag"]
            for item in input_circle_items:
                if self.canvas.gettags(item)[1] == dst_tag:
                    input_ID = item
            for item in output_circle_items:
                if self.canvas.gettags(item)[1] == src_tag:
                    output_ID = item


            self.arrow_line = self.canvas.create_line(1, 1 , 1, 1, width = 2, arrow=tk.LAST, tags="arrow")
            self.arrows.append((output_ID, input_ID, self.arrow_line, dst_tag, src_tag))
            self.arrow_line = None
        self.update_arrows()

        # init params
        for fx_param in fx_params:
            for xml_setting in fx_params_options[fx_param].attrib:
                settings = self.slidemenu.fx_parameters[fx_param.tag]['settings']
                value = fx_params_options[fx_param].attrib[xml_setting]
                settings[xml_setting].set(value)

        print("LOAD")

    def set_gen_location(self):
        print("set_gen_location")
        self.codegen_location_inc = filedialog.askdirectory(title="Select folder for .h")
        self.codegen_location_src = filedialog.askdirectory(title="Select folder for .src")

    def get_unique_block_tag(self):
        
        tags = []
        for block in self.blocks:
            tags.append(block.tag)
        while f"block{self.unique_num}" in tags:
            self.unique_num = self.unique_num + 1
        
        return f"block{self.unique_num}"

    def add_abs_block(self,tag = None, x=50, y=50, load_data=None):
        if tag is None:
            tag = self.get_unique_block_tag()

        new_block = sab_math.ABSBlock(self.canvas, tag,x=x,y=y, load_data=load_data)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks
    
    def add_lim_block(self,tag = None, x=50, y=50, load_data=None):
        if tag is None:
            tag = self.get_unique_block_tag()

        new_block = sab_math.LimitBlock(self.canvas, tag,x=x,y=y, load_data=load_data)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks
    
    def add_mavg_filter_block(self,tag = None, x=50, y=50, load_data=None):
        if tag is None:
            tag = self.get_unique_block_tag()

        new_block = sab_filters.MovingAverage(self.canvas, tag,x=x,y=y, load_data=load_data)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks

    def add_const_block(self,tag = None, x=50, y=50, load_data=None):
        if tag is None:
            tag = self.get_unique_block_tag()

        new_block = sab_math.ConstBlock(self.canvas, tag,x=x,y=y, load_data=load_data)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks

    def add_add_block(self,tag = None, x=50, y=50, load_data=None):
        if tag is None:
            tag = self.get_unique_block_tag()

        new_block = sab_math.AddBlock(self.canvas, tag,x=x,y=y, load_data=load_data)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks

    def add_mul_block(self,tag = None, x=50, y=50, load_data=None):
        if tag is None:
            tag = self.get_unique_block_tag()

        new_block = sab_math.MulBlock(self.canvas, tag,x=x,y=y, load_data=load_data)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks
    
    def add_div_block(self,tag = None, x=50, y=50, load_data=None):
        if tag is None:
            tag = self.get_unique_block_tag()

        new_block = sab_math.DivBlock(self.canvas, tag,x=x,y=y, load_data=load_data)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks
        
    def add_sub_block(self,tag = None, x=50, y=50, load_data=None):
        if tag is None:
            tag = self.get_unique_block_tag()

        new_block = sab_math.SubBlock(self.canvas, tag,x=x,y=y, load_data=load_data)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks
        

    def add_input_block(self,tag = None, x=50, y=50, load_data=None):
        if tag is None:
            tag = self.get_unique_block_tag()

        new_block = sab_io.InputBlock(self.canvas, tag,x=x,y=y, load_data=load_data)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks

    def add_output_block(self,tag = None, x=50, y=50, load_data=None):
        if tag is None:
            tag = self.get_unique_block_tag()

        new_block = sab_io.OutputBlock(self.canvas, tag,x=x,y=y, load_data=load_data)

        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks

    def add_generator_block(self,tag = None, x=50, y=50, load_data=None):
        if tag is None:
            tag = self.get_unique_block_tag()

        new_block = sab_io.GeneratorBlock(self.canvas, tag,x=x,y=y, load_data=load_data)

        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks

    def add_filterbank_block(self,tag = None, x=50, y=50, load_data=None):
        if tag is None:
            tag = self.get_unique_block_tag()

        new_block = sab_filters.FilterBank(self.canvas, tag,x=x,y=y, load_data=load_data)
    
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks
    
    def add_biquad_filter_block(self,tag = None, x=50, y=50, load_data=None):
        if tag is None:
            tag = self.get_unique_block_tag()

        new_block = sab_filters.BiquadFilter(self.canvas, tag,x=x,y=y, load_data=load_data)
    
        self.blocks.append(new_block)
        self.bind_events()  # Ensure

    def bind_events(self):
        # resize window
        self.canvas.bind("<Configure>", self.on_resize)

        # Bind events for dragging the canvas
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        # Bind events to blocks and circles
        self.canvas.tag_bind("block", "<ButtonPress-1>", self.on_block_press)
        self.canvas.tag_bind("block", "<B1-Motion>", self.on_block_drag)
        self.canvas.tag_bind("output_circle", "<ButtonPress-1>", self.on_output_circle_press)
        self.canvas.tag_bind("output_circle", "<Enter>", self.on_output_circle_hover)
        self.canvas.tag_bind("output_circle", "<Leave>", self.on_output_circle_leave)
        self.canvas.tag_bind("input_circle", "<Enter>", self.on_input_circle_hover)
        self.canvas.tag_bind("input_circle", "<Leave>", self.on_input_circle_leave)
        self.canvas.tag_bind("input_circle", "<ButtonPress-1>", self.on_input_circle_press)

        # Prevent circles from being dragged separately
        self.canvas.tag_bind("input_circle", "<B1-Motion>", lambda event: "break")
        self.canvas.tag_bind("output_circle", "<B1-Motion>", lambda event: "break")

        # Bind right-click to each block and arrow
        self.canvas.tag_bind("block", "<Button-3>", self.select_block)
        self.canvas.tag_bind("arrow", "<Button-3>", self.select_arrow)
         # Bind right-click to open the context menu
        self.canvas.bind("<Button-3>", self.show_context_menu)

    def on_resize(self, event=None):
        self.canvas.config(width=self.canvas.winfo_screenwidth(), height=self.canvas.winfo_screenheight())  
    
    # Code generation
    def generate_c_code(self):


        # Create a directed graph
        graph = nx.DiGraph()
        for arrow in self.arrows:
            graph.add_edge(arrow[4],arrow[3])

        builder = fx_builder.SAB_fx_builder()
        
        builder.generate_code(self.arrows,self.blocks,self.slidemenu.fx_parameters,output_path_src=self.codegen_location_src,output_path_inc=self.codegen_location_inc)
        pass

    def select_block(self, event):
        # Identify the selected block for deletion

        item = self.canvas.find_withtag("current")[0]
        tags = self.canvas.gettags(item)
        self.selected_block = tags[1]  # Assuming the second tag is the unique block identifier
        print("select_block: ", self.selected_block)

    def select_arrow(self, event):
        # Identify the selected arrow for deletion
        self.selected_arrow = self.canvas.find_withtag("current")[0]
        print("select_arrow")

    def delete_block(self,block_to_delete=None):
        if block_to_delete is not None:
            self.selected_block = block_to_delete
        if self.selected_block:
            # Delete assigned parameters!
            for block in self.blocks:
                if block.tag ==self.selected_block:
                    try:
                        for opt in block.option_vars:
                            try:
                                binded_param = block.option_vars[opt]['binded_src']
                                if(binded_param != None):
                                    self.slidemenu.free_control_parameter(binded_param)
                            except:
                                pass
                    except:
                        pass
                        
            
            
            # Delete arrows!
            for arrow in self.arrows[:]:
                if arrow[3] == self.selected_block or arrow[4] == self.selected_block:
                    self.canvas.delete(arrow[2])
                    self.arrows.remove(arrow)
                    

            # Delete blocks!
            items = self.canvas.find_withtag(self.selected_block)
            for item in items[:]:
                self.canvas.delete(item)
            
            for block in self.blocks[:]:
                if(block.tag == self.selected_block):
                    self.blocks.remove(block)
            # Remove the selected block and associated items
            self.selected_block = None


    def reset_controls(self):
        # Delete assigned parameters!
        for block in self.blocks:
            if block.tag ==self.selected_block:
                try:
                    for opt in block.option_vars:
                        try:
                            binded_param = block.option_vars[opt]['binded_src']
                            if(binded_param != None):
                                self.slidemenu.free_control_parameter(binded_param)
                                block.option_vars[opt]['binded_src'] = None
                                block.option_vars[opt]['var'].set(block.option_vars[opt]['default_value'])
                        except:
                            pass
                except:
                    pass

    def delete_arrow(self):
        if self.selected_arrow:
            # Remove the selected arrow
            self.canvas.delete(self.selected_arrow)
            for arrow in self.arrows:
                if(arrow[2] == self.selected_arrow):
                    self.arrows.remove(arrow)
            self.selected_arrow = None

    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)

    def get_options_by_tag(self,tag_to_find):
        for block in self.blocks:
            if block.tag == tag_to_find:
                return block.option_vars
        return None

    def iterate_stringvars(self, data):
        for key, value in data.items():
            print(f"Processing key: {key}")
            
            if isinstance(value, dict):  # Check if the value is a dictionary
                stringvar = value.get('var')  # Access the 'var' key for StringVar
                if isinstance(stringvar, tk.StringVar):  # Check if it's a StringVar
                    print(f"  StringVar found for '{key}':")
                    print(f"    Current Value: {stringvar.get()}")

                    # Now print the other parameters in the dictionary
                    print(f"    min_value: {value.get('min_value', 'N/A')}")
                    print(f"    max_value: {value.get('max_value', 'N/A')}")
                    print(f"    default_value: {value.get('default_value', 'N/A')}")
                else:
                    print(f"  No StringVar found for '{key}', moving on...")

    def on_block_press(self, event):
        print("on_block_press")
        item = self.canvas.find_withtag("current")[0]
        tags = self.canvas.gettags(item)
        self.drag_data = {"x": event.x, "y": event.y, "item": item, "tags": tags}
        self.slidemenu.block_settings_load(self.get_options_by_tag(tags[1]))
        try:
            print(self.get_options_by_tag(tags[1]))
            print(len(self.get_options_by_tag(tags[1])))
            self.iterate_stringvars(self.get_options_by_tag(tags[1]))
            for name in self.get_options_by_tag(tags[1]):
                print(name)
        except:
            pass

    def on_block_drag(self, event):
        print("on_block_drag")
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
        try:
            # Move only the items associated with the clicked block
            unique_tag = self.drag_data["tags"][1]  # Assuming the second tag is the unique block identifier
            items = self.canvas.find_withtag(unique_tag)
            for item in items:
                self.canvas.move(item, dx, dy)
        except:
            pass

        self.update_arrows()
        

    def on_output_circle_press(self, event):
        print("on_output_circle_press")
        # Start the arrow from the output circle
        self.selected_output_circle = self.canvas.find_withtag("current")[0]
        print("self.selected_output_circle: ",self.selected_output_circle)
        x1, y1, x2, y2 = self.canvas.coords(self.selected_output_circle)
        self.arrow_line = self.canvas.create_line((x1 + x2) / 2, (y1 + y2) / 2, event.x, event.y, width = 2, arrow=tk.LAST, tags="arrow")
        self.canvas.bind("<Motion>", self.on_arrow_drag)
        self.canvas.bind("<ButtonPress-1>", self.on_canvas_click)

    def on_arrow_drag(self, event):
        # print("on_arrow_drag")
        # Update the arrow's endpoint to follow the mouse
        if self.arrow_line:
            x1, y1, x2, y2 = self.canvas.coords(self.selected_output_circle)
            self.canvas.coords(self.arrow_line, (x1 + x2) / 2, (y1 + y2) / 2, event.x, event.y)

    def on_canvas_click(self, event):
        print("on_canvas_click")
        # Detect click events on the canvas during arrow drawing
        overlapping_items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        for item in overlapping_items:
            item_tags = self.canvas.gettags(item)
            print(f"Item under cursor: {item}, tags: {item_tags}")
            if "output_circle" in item_tags:
                self.selected_output_circle_block = item_tags[1]
                return
            if "input_circle" in item_tags:
                self.selected_input_circle_block = item_tags[1]
                self.on_input_circle_press(event)
                return

    def on_output_circle_hover(self, event):
        print("on_output_circle_hover")
        # Highlight the output circle when hovered over
        current_circle = self.canvas.find_withtag("current")[0]
        print(self.canvas.coords(current_circle))
        self.canvas.itemconfig(current_circle, outline="red", width=2)

    def on_input_circle_hover(self, event):
        print("on_input_circle_hover")
        # Highlight the input circle when hovered over
        current_circle = self.canvas.find_withtag("current")[0]
        print(self.canvas.coords(current_circle))
        self.canvas.itemconfig(current_circle, outline="red", width=2)

    def on_output_circle_leave(self, event):
        print("on_output_circle_leave")
        # Remove highlight from the output circle when not hovered
        current_circle = self.canvas.find_withtag("current")[0]
        self.canvas.itemconfig(current_circle, outline="", width=1)

    def on_input_circle_leave(self, event):
        print("on_input_circle_leave")
        # Remove highlight from the input circle when not hovered
        current_circle = self.canvas.find_withtag("current")[0]
        self.canvas.itemconfig(current_circle, outline="", width=1)
    

    # TODO: When blcoks are dragged the IO cirlces are NOT updated!!! Circle positions must be updated!!!
    def on_input_circle_press(self, event):
        print("***** on_input_circle_press: ", self.selected_output_circle)
        # Connect the arrow to the input circle if it exists
        if self.arrow_line:
            target_input_circle = self.canvas.find_withtag("current")[0]
            overlapping_items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
            for item in overlapping_items:
                item_tags = self.canvas.gettags(item)
                
                print(f"Item under cursor: {item}, tags: {item_tags}")
                print("***** on_input_circle_press: ", self.selected_output_circle)
                if "input_circle" in item_tags:
                    try:
                        x1, y1, x2, y2 = self.canvas.coords(self.selected_output_circle)
                    except:
                        print("EXCEPTION: ", self.selected_output_circle)
                    
                    x3, y3, x4, y4 = self.canvas.coords(target_input_circle)
                    self.arrows.append((self.selected_output_circle, item, self.arrow_line, self.selected_input_circle_block, self.selected_output_circle_block))
                    self.arrow_line = None
                    self.selected_output_circle = None
                    print("connected")
                    break
                else:
                    print("on_input_circle_press ELSE")
                    # self.cancel_arrow(event)

    def cancel_arrow(self, event):
        print("cancel_arrow")
        # Cancel the arrow drawing
        if self.arrow_line:
            self.canvas.delete(self.arrow_line)
            self.arrow_line = None
            self.selected_output_circle = None

    def update_arrows(self):
        # Update the arrow positions
        print("update arrows STARTED...")
        for arrow in self.arrows:
            start_circle    = arrow[0]
            end_circle      = arrow[1]
            line            = arrow[2]

            print("start circle: ", start_circle)
            print("end_circle",     end_circle)
            print("line:",          line)
            print(self.canvas.coords(start_circle))
            print(self.canvas.coords(end_circle))
            x1, y1, x2, y2 = self.canvas.coords(start_circle)
            x3, y3, x4, y4 = self.canvas.coords(end_circle)
            
            self.canvas.coords(line, (x1 + x2) / 2, (y1 + y2) / 2, (x3 + x4) / 2, (y3 + y4) / 2)

        print("update arrows FINISHED")

    def on_click(self, event):
        print("on_click")
        # Record the initial position of the click
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_drag(self, event):
        # print("on_drag")
        delta_x = 0
        delta_y = 0
        # Calculate how much the mouse has moved
        if (self.drag_data["x"] == 0):
           pass
        
        else:
            delta_x = event.x - self.drag_data["x"]
            delta_y = event.y - self.drag_data["y"]  

        # Move the canvas by the deltamax_value
        self.canvas.move(tk.ALL, delta_x, delta_y)

        # Update the recorded position
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_release(self, event):
        print("on_release")
        # Reset the drag data
        self.drag_data = {"x": 0, "y": 0, "item": None, "tags": None}


if __name__ == "__main__":
    root = tk.Tk()
    app = CodeGeneratorApp(root)

    

    root.mainloop()


