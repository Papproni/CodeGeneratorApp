import tkinter as tk

class SlideMenu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.menu_visible = False

        # Configure the main window
        self.parent.geometry("600x300")
        self.parent.bind("3", self.toggle_menu)  # Bind "3" key
        self.parent.bind("<Configure>", self.on_resize)  # Bind the window resize event to the on_resize function

        # Create a Frame for the side menu
        self.menu_frame = tk.Frame(self.parent, width=400, bg="#333333")

        # Add a scrollbar to the menu frame
        self.scrollbar = tk.Scrollbar(self.menu_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a canvas to hold the buttons and enable scrolling
        self.canvas = tk.Canvas(self.menu_frame, yscrollcommand=self.scrollbar.set, bg="#333333")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure scrollbar to work with the canvas
        self.scrollbar.config(command=self.canvas.yview)

        # Create a frame inside the canvas to hold the content
        self.content_frame = tk.Frame(self.canvas, bg="#333333")
        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

        # Add close button
        self.close_button = tk.Button(self.content_frame, text="Close", command=self.toggle_menu, 
                                      bg="#444444", fg="white", font=("Arial", 10, "bold"))
        self.close_button.grid(row=0, column=0, columnspan=6, pady=10, padx=10, sticky="e")

        # Add "slots" in the layout described
        self.add_menu_slots()

        # Ensure the content frame is correctly sized
        self.content_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Initial placement of the menu (hidden initially)
        self.menu_frame.place(x=self.parent.winfo_width(), y=0, height=self.parent.winfo_height())

    def add_menu_slots(self):
        # Create a grid with "slots" as described

        # Page 1 slots
        slots_page1 = [
            ("P1", "P2", "P3"),
            ("P4", "P5", "P6")
        ]

        # Page 2 slots
        slots_page2 = [
            ("P7", "P8", "P9"),
            ("P10", "P11", "P12")
        ]

        # Function to create a slot (square)
        def create_slot(parent, slot_name):
            frame = tk.Frame(parent, width=70, height=70, bg="#555555", relief="ridge", bd=2)
            frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents

            # Textbox in the middle for the parameter name (default "None")
            textbox = tk.Entry(frame, justify="center", font=("Arial", 10))
            textbox.insert(0, "None")
            textbox.pack(expand=True)

            # Label at the bottom for the slot name
            label = tk.Label(frame, text=slot_name, bg="#555555", fg="white", font=("Arial", 10, "bold"))
            label.pack(side="bottom")

            return frame

        # Display Page 1 slots
        row_offset = 1  # Start after the close button
        for row in range(2):
            for col in range(3):
                slot_text = slots_page1[row][col]
                slot_frame = create_slot(self.content_frame, slot_text)
                slot_frame.grid(row=row + row_offset, column=col, padx=15, pady=15)

        # Label for Page 1
        page1_label = tk.Label(self.content_frame, text="Page 1", bg="#333333", fg="white", font=("Arial", 12, "bold"))
        page1_label.grid(row=row_offset + 2, column=0, columnspan=3, pady=(20, 10))

        # Display Page 2 slots
        row_offset += 3  # Adjust the row offset for Page 2
        for row in range(2):
            for col in range(3):
                slot_text = slots_page2[row][col]
                slot_frame = create_slot(self.content_frame, slot_text)
                slot_frame.grid(row=row + row_offset, column=col, padx=15, pady=15)

        # Label for Page 2
        page2_label = tk.Label(self.content_frame, text="Page 2", bg="#333333", fg="white", font=("Arial", 12, "bold"))
        page2_label.grid(row=row_offset + 2, column=0, columnspan=3, pady=(20, 10))

    def menu_item_selected(self, slot):
        # Define what happens when a slot is clicked
        print(f"Slot {slot} selected")
        # You can add more functionality here, e.g., updating the main window, opening a dialog, etc.

    def toggle_menu(self, event=None):
        # Update the height of the menu to match the window's height
        self.menu_frame.config(height=self.parent.winfo_height())
        
        if self.menu_visible:
            self.menu_frame.place(x=self.parent.winfo_width(), y=0)
            self.menu_visible = False
        else:
            self.menu_frame.place(x=self.parent.winfo_width() - 400, y=0)
            self.menu_visible = True
    def on_resize(self, event=None):
        new_height = self.parent.winfo_height()
        # Adjust the position of the menu if it's visible
        if self.menu_visible:
            self.menu_frame.place(x=self.parent.winfo_width() - 400, y=0, height=new_height)
        else:
            self.menu_frame.place(x=self.parent.winfo_width(), y=0)

if __name__ == "__main__":
    root = tk.Tk()
    app = SlideMenu(root)
    root.mainloop()
