import tkinter as tk
from tkinter import Canvas, Menu, StringVar, OptionMenu

# BLOCKS
# import sab_filters
# import sab_io
from gui_blocks import sab_filters
from gui_blocks import sab_io
from gui_blocks import sab_math

import fx_builder

import slidemenu

import networkx as nx

# On screen user has 6 options to use
# maximum 12 options are available
# each slot can be a "checkbox" or a "potentiometer"

# In gui user must choose a parameter assign it to a one of above
# USER MUST: Set a name for the parameter
# IF potentiometer is choosen:
    # he must choose Min and Max Value
    # on the menu user must choose a place on the screen
    # User can chage parameters on screen according to position (IE: on P1 and P7 = POT1)
    # User can set potentiometer variable to Side, if thats needed, the outside control must be used!

# IF checkbox is choosen 
    # he must choose Min and Max Value for checked and unchecked box (touch)
    # on the menu user must choose a place on the screen 


#
# *-------------------*    *-------------------*
# |  P1  |  P2  |  P3  |    |  P7  |  P8  |  P9  |
# |--------------------|    |--------------------|
# |  P4  |  P5  |  P6  |    |  P10 |  P11 | P12  |
# *-------------------*    *-------------------*
#         Page 1                    Page 2

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
        self.root.wm_attributes("-topmost", True)
        root.geometry("1000x1000")

        self.canvas = Canvas(root, width=800, height=800, bg="white")
        self.canvas.pack()

        self.slidemenu = slidemenu.SlideMenu(root,self.generate_c_code)

        self.blocks = []
        self.arrows = []
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



    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        io_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="IO", menu=io_menu)

        io_menu.add_command(label="Input", command=self.add_input_block)
        io_menu.add_command(label="Output", command=self.add_output_block)

        filter_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Filters", menu=filter_menu)
        filter_menu.add_command(label="Filterbank", command=self.add_filterbank_block)
        filter_menu.add_command(label="Biquad",     command=self.add_biquad_filter_block)
        filter_menu.add_command(label="Moving Avg", command=self.add_mavg_filter_block)


        math_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Math", menu=math_menu)
        
        math_menu.add_command(label="Const",    command=self.add_Const_block)
        math_menu.add_command(label="Add",      command=self.add_Add_block)
        math_menu.add_command(label="Mul",      command=self.add_Mul_block)
        math_menu.add_command(label="Div",      command=self.add_Div_block)
        math_menu.add_command(label="Sub",      command=self.add_Sub_block)
        math_menu.add_command(label="Lim",      command=self.add_Lim_block)
        math_menu.add_command(label="ABS",      command=self.add_ABS_block)
        
        special_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Special", menu=special_menu)
        
        special_menu.add_command(label="Generator",     command=self.add_Add_block)
        special_menu.add_command(label="Delay line",    command=self.add_Add_block)
        special_menu.add_command(label="Reverb",        command=self.add_Add_block)
        special_menu.add_command(label="PitchShift",    command=self.add_Add_block)
        
        special_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Control", menu=special_menu)
        
        special_menu.add_command(label="PID",                       command=self.add_Add_block)
        special_menu.add_command(label="State Space Control",       command=self.add_Add_block)

    def get_unique_block_tag(self):
        self.unique_num = self.unique_num + 1 
        return f"block{self.unique_num}"

    def add_ABS_block(self,x=50, y=50):
        tag = self.get_unique_block_tag()

        new_block = sab_math.ABSBlock(self.canvas,tag)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks
    
    def add_Lim_block(self,x=50, y=50):
        tag = self.get_unique_block_tag()

        new_block = sab_math.LimitBlock(self.canvas,tag)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks
    
    def add_mavg_filter_block(self,x=50, y=50):
        tag = self.get_unique_block_tag()

        new_block = sab_filters.MovingAverage(self.canvas,tag)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks

    def add_Const_block(self, x=50, y=50):
        tag = self.get_unique_block_tag()

        new_block = sab_math.ConstBlock(self.canvas,tag)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks

    def add_Add_block(self, x=50, y=50):
        tag = self.get_unique_block_tag()

        new_block = sab_math.AddBlock(self.canvas,tag)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks

    def add_Mul_block(self, x=50, y=50):
        tag = self.get_unique_block_tag()

        new_block = sab_math.MulBlock(self.canvas,tag)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks
    
    def add_Div_block(self, x=50, y=50):
        tag = self.get_unique_block_tag()

        new_block = sab_math.DivBlock(self.canvas,tag)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks
        
    def add_Sub_block(self, x=50, y=50):
        tag = self.get_unique_block_tag()

        new_block = sab_math.SubBlock(self.canvas,tag)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks
        

    def add_input_block(self, x=50, y=50):
        tag = self.get_unique_block_tag()

        new_block = sab_io.InputBlock(self.canvas,tag)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks

    def add_output_block(self, x=200, y=150):
        tag = self.get_unique_block_tag()

        new_block = sab_io.OutputBlock(self.canvas,tag)

        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks

    def add_filterbank_block(self, x=200, y=150):
        tag = self.get_unique_block_tag()

        new_block = sab_filters.FilterBank(self.canvas,tag)
    
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks
    
    def add_biquad_filter_block(self, x=200, y=200):
        tag = self.get_unique_block_tag()

        new_block = sab_filters.BiquadFilter(self.canvas,tag)
    
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


        # Find INPUT blocks
        # Find tag ID of their output_circles in arrows
        # Check which ID does the arrow connect to etc
        # self.generation_sequence = None
        # self.generation_sequence = {}
        # Make a block order
        # the order starts with INPUT block
        # Insert list
        # Find the connections that this block is connected to (1 or multiple) put them in a list
        # path_num = 0
        
        # # FInd input blocks
        # for block in self.blocks:
        #     if(block.type == "INPUT_BLOCK"):
        #         start_node = block.tag
        #         self.generation_sequence[path_num] = []
        #         self.generation_sequence[path_num].append({"tag":block.tag,"type":block.type})
        #         path_num = path_num + 1
        #     if(block.type == "OUTPUT_BLOCK"):
        #         end_node  = block.tag

        # path = nx.shortest_path(graph, source=start_node, target=end_node)
        # print(list(nx.all_simple_paths(graph,source=start_node, target=end_node )))
        # paths = list(nx.all_simple_paths(graph,source=start_node, target=end_node ))
        builder = fx_builder.SAB_fx_builder()
        
        builder.generate_code(self.arrows,self.blocks,self.slidemenu.fx_parameters)
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

    def delete_block(self):
        if self.selected_block:
            # Delete assigned parameters!
            for block in self.blocks:
                if block.tag ==self.selected_block:
                    try:
                        for opt in block.option_vars:
                                binded_param = block.option_vars[opt]['binded_src']
                                if(binded_param != None):
                                    self.slidemenu.free_control_parameter(binded_param)
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
                    # self.canvas.coords(self.arrow_line, (x1 + x2)/2, (y1 + y2)/2, (x3 + x4) / 2, (y3 + y4) / 2)
                    self.arrows.append((self.selected_output_circle, item, self.arrow_line, self.selected_input_circle_block, self.selected_output_circle_block))
                    self.arrow_line = None
                    self.selected_output_circle = None
                    # self.canvas.unbind("<Motion>")
                    # self.canvas.unbind("<ButtonPress-1>")
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
            # self.canvas.unbind("<Motion>")
            # self.canvas.unbind("<ButtonPress-1>")

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


