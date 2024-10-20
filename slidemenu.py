import tkinter as tk

class SlideMenu(tk.Frame):
    def __init__(self, parent,code_gen_func):
        super().__init__(parent)
        self.parent         = parent
        self.code_gen_func  = code_gen_func
        self.menu_visible   = False

        # Configure the main window
        self.parent.geometry("600x300")
        self.parent.bind("+", self.toggle_menu)  # Bind "3" key
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
      
        self.add_buttons()
        # Add "slots" in the layout described
        self.add_menu_slots()

        settings = [
            ("Cutoff Frequency",    "NUM", 1000),  # in Hz
            ("Resonance",           "NUM", 0.7)          # Q factor        # Bypass the filter: ON or OFF
        ]
        
        # self.block_settings_load(settings)
        
        # Ensure the content frame is correctly sized
        self.content_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
    
        # Initial placement of the menu (hidden initially)
        self.menu_frame.place(x=self.parent.winfo_width(), y=0, height=self.parent.winfo_height())

        
    def add_buttons(self):
        self.content_frame = tk.Frame(self.canvas, bg="#333333")
        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")
        
        # Add CLOSE button
        self.close_button = tk.Button(self.content_frame, text="Close", command=self.toggle_menu, 
                                      bg="#444444", fg="white", font=("Arial", 10, "bold"))
        self.close_button.grid(row=0, column=0, columnspan=6, pady=10, padx=10, sticky="e")

        # Add GENERATE button
        self.generate_btn = tk.Button(self.content_frame, 
                                      text="GENERATE CODE", command=self.code_gen_func, 
                                      bg="#044444", fg="white", font=("Arial", 10, "bold"))
        self.generate_btn.grid(row=0, column=0, columnspan=6, pady=10, padx=100, sticky="e")

    def block_settings_load(self, settings):
        # If a settings frame already exists, destroy it to avoid stacking
        if hasattr(self, 'settings_frame') and self.settings_frame.winfo_exists():
            self.settings_frame.destroy()

        # Calculate the starting row for settings after the slots have been added
        current_row = len(self.content_frame.grid_slaves())  # Get the next available row after all slots are added

        # Create a frame for the settings section with a grey background
        self.settings_frame = tk.Frame(self.content_frame, bg="#4f4f4f")  # Dark grey background
        self.settings_frame.grid(row=current_row, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Add a title for the settings
        title_label = tk.Label(self.settings_frame, text="Settings", bg="#4f4f4f", fg="white", font=("Arial", 14, "bold"))
        title_label.pack(pady=10)  # Add some padding for the title

        # Now add each setting inside the settings frame
        for i, (name, setting_type, value) in enumerate(settings):
            # Create a sub-frame to hold each setting item
            frame = tk.Frame(self.settings_frame, width=200, height=50, bg="#333333", relief="ridge", bd=2)
            frame.pack(fill="x", padx=10, pady=5)
            frame.pack_propagate(False)  # Prevent the frame from resizing to fit contents

            # Create label for the setting name
            label = tk.Label(frame, text=name, bg="#333333", fg="white", font=("Arial", 10, "bold"))
            label.pack(side=tk.LEFT, padx=10)

            if setting_type == "NUM":
                # Create an Entry widget for numeric input
                entry = tk.Entry(frame, width=10)
                entry.insert(0, str(value))  # Insert the default value into the entry box
                entry.pack(side=tk.RIGHT, padx=10)

            elif setting_type == "BTN":
                # Create a Button with the initial value (e.g., "ON" or "OFF")
                button = tk.Button(frame, text=value, width=10, bg="#555555", fg="white", font=("Arial", 10, "bold"))
                button.pack(side=tk.RIGHT, padx=10)

            # Update the canvas scroll region after adding the settings
            self.content_frame.update_idletasks()  # Ensure all widgets are rendered
            self.canvas.config(scrollregion=self.canvas.bbox("all"))  # Update the scroll region



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
            textbox = tk.Button(frame, 
                                      text="Add", command=self.code_gen_func, 
                                      bg="#042344", fg="white", font=("Arial", 10, "bold"))
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
        page2_label.grid(row=row_offset + 2, column=0, columnspan=3, pady=(0, 10))

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
        new_height  = self.parent.winfo_height()
        new_width   = self.parent.winfo_width()
        
        # Adjust the position of the menu if it's visible
        if self.menu_visible:
            self.menu_frame.place(x=new_width - 400, y=0, height=new_height)
        else:
            self.menu_frame.place(x=new_width, y=0)

if __name__ == "__main__":
    root = tk.Tk()
    app = SlideMenu(root)
    root.mainloop()
