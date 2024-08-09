import tkinter as tk
from tkinter import Canvas, Menu

# BLOCKS
import input_block
import output_block

class CodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DSP code gen for STM AUDIO BOARD V3")
        self.canvas = Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.blocks = []
        self.arrows = []
        self.selected_output_circle = None
        self.arrow_line = None
        self.drag_data = {"x": 0, "y": 0, "item": None, "tags": None}

        self.create_menu()
        self.bind_events()
        self.root.bind("<Escape>", self.cancel_arrow)

    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        io_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="IO", menu=io_menu)

        io_menu.add_command(label="Input", command=self.add_input_block)
        io_menu.add_command(label="Output", command=self.add_output_block)

    def add_input_block(self, x=50, y=50):
        block_id = len(self.blocks) + 1
        tag = f"block{block_id}"

        new_block = input_block.InputBlock(self.canvas,tag)
        
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks

    def add_output_block(self, x=200, y=150):
        block_id = len(self.blocks) + 1
        tag = f"block{block_id}"

        new_block = output_block.OutputBlock(self.canvas,tag)
      
        self.blocks.append(new_block)
        self.bind_events()  # Ensure events are bound after adding blocks

    def bind_events(self):
        # Bind events to blocks and circles
        self.canvas.tag_bind("block", "<ButtonPress-1>", self.on_block_press)
        self.canvas.tag_bind("block", "<B1-Motion>", self.on_block_drag)
        self.canvas.tag_bind("output_circle", "<ButtonPress-1>", self.on_output_circle_press)
        self.canvas.tag_bind("input_circle", "<Enter>", self.on_input_circle_hover)
        self.canvas.tag_bind("input_circle", "<Leave>", self.on_input_circle_leave)
        self.canvas.tag_bind("input_circle", "<ButtonPress-1>", self.on_input_circle_press)

        # Prevent circles from being dragged separately
        self.canvas.tag_bind("input_circle", "<B1-Motion>", lambda event: "break")
        self.canvas.tag_bind("output_circle", "<B1-Motion>", lambda event: "break")

    def on_block_press(self, event):
        item = self.canvas.find_withtag("current")[0]
        tags = self.canvas.gettags(item)
        self.drag_data = {"x": event.x, "y": event.y, "item": item, "tags": tags}

    def on_block_drag(self, event):
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

        # Move only the items associated with the clicked block
        unique_tag = self.drag_data["tags"][1]  # Assuming the second tag is the unique block identifier
        items = self.canvas.find_withtag(unique_tag)
        for item in items:
            self.canvas.move(item, dx, dy)
        self.update_arrows()

    def on_output_circle_press(self, event):
        print("on_output_circle_press")
        # Start the arrow from the output circle
        self.selected_output_circle = self.canvas.find_withtag("current")[0]
        x1, y1, x2, y2 = self.canvas.coords(self.selected_output_circle)
        self.arrow_line = self.canvas.create_line((x1 + x2) / 2, (y1 + y2) / 2, event.x, event.y, arrow=tk.LAST, tags="arrow")
        self.canvas.bind("<Motion>", self.on_arrow_drag)
        self.canvas.bind("<ButtonPress-1>", self.on_canvas_click)

    def on_arrow_drag(self, event):
        print("on_arrow_drag")
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
            if "input_circle" in item_tags:
                self.on_input_circle_press(event)
                return

    def on_input_circle_hover(self, event):
        print("on_input_circle_hover")
        # Highlight the input circle when hovered over
        current_circle = self.canvas.find_withtag("current")[0]
        self.canvas.itemconfig(current_circle, outline="red", width=2)

    def on_input_circle_leave(self, event):
        print("on_input_circle_leave")
        # Remove highlight from the input circle when not hovered
        current_circle = self.canvas.find_withtag("current")[0]
        self.canvas.itemconfig(current_circle, outline="", width=1)

    def on_input_circle_press(self, event):
        print("on_input_circle_press")
        # Connect the arrow to the input circle if it exists
        if self.arrow_line:
            target_input_circle = self.canvas.find_withtag("current")[0]
            overlapping_items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
            for item in overlapping_items:
                item_tags = self.canvas.gettags(item)
                print(f"Item under cursor: {item}, tags: {item_tags}")
                if "input_circle" in item_tags:
                    print("connected")
                    x1, y1, x2, y2 = self.canvas.coords(self.selected_output_circle)
                    x3, y3, x4, y4 = self.canvas.coords(target_input_circle)
                    self.canvas.coords(self.arrow_line, (x1 + x2) / 2, (y1 + y2) / 2, (x3 + x4) / 2, (y3 + y4) / 2)
                    self.arrows.append((self.selected_output_circle, target_input_circle, self.arrow_line))
                    self.arrow_line = None
                    self.selected_output_circle = None
                    self.canvas.unbind("<Motion>")
                    self.canvas.unbind("<ButtonPress-1>")
                else:
                    print("cancel_arrow")
                    self.cancel_arrow(event)

    def cancel_arrow(self, event):
        # Cancel the arrow drawing
        if self.arrow_line:
            self.canvas.delete(self.arrow_line)
            self.arrow_line = None
            self.selected_output_circle = None
            self.canvas.unbind("<Motion>")
            self.canvas.unbind("<ButtonPress-1>")

    def update_arrows(self):
        # Update the arrow positions
        for arrow in self.arrows:
            start_circle = arrow[0]
            end_circle = arrow[1]
            line = arrow[2]
            x1, y1, x2, y2 = self.canvas.coords(start_circle)
            x3, y3, x4, y4 = self.canvas.coords(end_circle)
            self.canvas.coords(line, (x1 + x2) / 2, (y1 + y2) / 2, (x3 + x4) / 2, (y3 + y4) / 2)

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeGeneratorApp(root)
    # app.add_input_block(50, 50)  # Add an initial input block
    # app.add_output_block(200, 150)  # Add an initial output block
    root.mainloop()
