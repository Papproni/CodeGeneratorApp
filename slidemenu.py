import tkinter as tk

class SlideMenu(tk.Frame):
    def __init__(self, parent,code_gen_func):
        super().__init__(parent)
        self.parent         = parent
        self.code_gen_func  = code_gen_func
        self.menu_visible   = True # SET THIS FALSE IN FINAL

        self.current_parameter_clicked  = None
        self.setting_choosen            = None
        self.parameter_choosing_state   = tk.BooleanVar(value=False)
        # Configure the main window
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
    
    def on_hover(self, event):
        if(self.parameter_choosing_state.get() == True):
            event.widget.config(bg="yellow")  # Change background to yellow on hover

    def on_leave(self, event):
        if(self.parameter_choosing_state.get() == True):
            event.widget.config(bg="lightblue")  # Revert to original background color
        else:
            event.widget.config(bg="#333333")
    def on_left_click(self,event,setting_data):
        if( self.parameter_choosing_state.get() == True):
            self.fx_parameters[self.current_parameter_clicked]['assigned_block_setting'] = setting_data
            key, data = setting_data
            self.fx_parameters[self.current_parameter_clicked]['var'].set(key)
            self.fx_parameters[self.current_parameter_clicked]['settings']['display_name'].set(key)
            setting_data[1]['binded_src'] = self.current_parameter_clicked
            setting_data[1]['var'].set(self.current_parameter_clicked)
            self.parameter_choosing_state.set(False)

    def control_param_settings_load(self, settings):
        
        self.parameter_choosing_state.set(False)
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

        def render_param(name, svar):
            frame = tk.Frame(self.settings_frame, width=200, height=50, bg="#333333", relief="ridge", bd=2)
            frame.pack(fill="x", padx=10, pady=5)
            frame.pack_propagate(False)  # Prevent the frame from resizing to fit contents
            label = tk.Label(frame, text=name, bg="#333333", fg="white", font=("Arial", 10, "bold"))
            label.pack(side=tk.LEFT, padx=10)
            entry = tk.Entry(frame, width=10, textvariable=svar)
            # Bind the validation based on the option type
            entry.pack(side=tk.RIGHT, padx=10)
        for setting in settings['settings']:
            svar = settings['settings'][setting]
            render_param(setting,svar)
        # render_params('min_value',settings['min_value'])
        # render_params('max_value',settings['max_value'])


    def block_settings_load(self, settings):
        
        self.parameter_choosing_state.set(False)
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

        self.settings = settings
        # Now add each setting inside the settings frame
        for  item in settings.items():
            # Create a sub-frame to hold each setting item
          
            key, data = item
            
            settings_stringvar = data['var']
            setting_type    = data['type']
            setting_name    = key
            name = key.lower()
            frame = tk.Frame(self.settings_frame, name = name, width=200, height=50, bg="#333333", relief="ridge", bd=2)
            # Bind hover events
           
            
            frame.pack(fill="x", padx=10, pady=5)
            frame.pack_propagate(False)  # Prevent the frame from resizing to fit contents
            # Create label for the setting name
            label = tk.Label(frame, text=setting_name, bg="#333333", fg="white", font=("Arial", 10, "bold"))
            label.pack(side=tk.LEFT, padx=10)


            if setting_type == "NUM":
                if(data['bindable'] != False):
                    frame.bind("<Enter>", self.on_hover)  # Mouse enters the frame
                    frame.bind("<Leave>", self.on_leave)  # Mouse leaves the frame
                    frame.bind("<Button-1>", lambda event, current_item=item: self.on_left_click(event, current_item))
                entry = tk.Entry(frame, width=10, textvariable=settings_stringvar)
                # Bind the validation based on the option type
                entry.pack(side=tk.RIGHT, padx=10)

            elif setting_type == "OPTIONBOX":
                # Create a Button with the initial value (e.g., "ON" or "OFF")
                # button = tk.Button(frame, text=settings_stringvar, width=10, bg="#555555", fg="white", font=("Arial", 10, "bold"))
                # button.pack(side=tk.RIGHT, padx=10)
                options = data['default_value'].split(",")
                option_menu = tk.OptionMenu(frame, settings_stringvar,  *options)
                option_menu.pack(side=tk.RIGHT, padx=10)
            elif setting_type == "TICKBOX":
                # Create a Button with the initial value (e.g., "ON" or "OFF")
                checkbutton = tk.Checkbutton(frame, variable=settings_stringvar)
                checkbutton.pack(side=tk.RIGHT, padx=10)
            elif setting_type == "CONTROL_PARAMETER":
                pass

            # Update the canvas scroll region after adding the settings
        self.content_frame.update_idletasks()  # Ensure all widgets are rendered
        self.canvas.config(scrollregion=self.canvas.bbox("all"))  # Update the scroll region

    def control_param_clicked(self,event):
        print("control_param_clicked")

        clicked_widget = event.widget

        # Retrieve the name of the widget
        button_name = clicked_widget.winfo_name()

        print(f"Right-clicked on button: {button_name}")

        # Perform actions based on the button name
        # Example: Access parameters if stored in a dictionary
        if button_name in self.fx_parameters:
            params = self.fx_parameters[button_name]
            print(f"Parameters for {button_name}: {params}")
            self.control_param_settings_load(params)

    def control_parameter_callback(self, parameter_clicked):
        print("control_parameter_add")
        print(parameter_clicked.get('param_name'))
        self.current_parameter_clicked = parameter_clicked.get('param_name')
        self.parameter_choosing_state.set(True)
        for item in self.settings.items():
            key, data = item
            if( data["bindable"] != False ):
                name = key.lower()
                self.settings_frame.children[name].config(bg = "lightblue" )
                pass
    
    def free_control_parameter(self,parameter):
        self.fx_parameters[parameter]['assigned_block_setting'] = None
        default = self.fx_parameters[self.current_parameter_clicked]['default_value']
        self.fx_parameters[self.current_parameter_clicked]['var'].set(default)
        self.fx_parameters[self.current_parameter_clicked]['settings']['display_name'].set(default)



    def add_menu_slots(self):
        self.fx_parameters = {}
        for i in range(12):
            var = tk.StringVar(value="Add")
            min_value = tk.StringVar(value=0)
            max_value = tk.StringVar(value=1)
            display_name = tk.StringVar(value="None")
            self.fx_parameters[f'param_{i+1}'] = {
                "var": var,
                "default_value": None,
                "param_name": f'param_{i+1}',
                "assigned_block_tag": None,
                "assigned_block_setting": None,
                "settings": {
                    "min_value": min_value,
                    "max_value": max_value,
                    "display_name": display_name,
                },
                "type": "CONTROL_PARAMETER"
            }
        # Create a grid with "slots" as described



        # Function to create a slot (square)
        def create_slot(parent, slot_name,parameter):
            frame = tk.Frame(parent,  width=70, height=70, bg="#000555", relief="ridge", bd=2) #tags=("control_parameter",slot_name)
            frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents

            # self.canvas.create_window(70, 70,tags=("control_parameter", slot_name))
            # self.canvas.bind("<ButtonPress-1>", self.control_param_clicked)



            # Textbox in the middle for the parameter name (default "None")
            textbox = tk.Button(frame, width=20, height=20, name = slot_name,
                                      textvariable=parameter['settings']["display_name"], command=lambda: self.control_parameter_callback(parameter), 
                                      bg="#042344", fg="white", font=("Arial", 10, "bold"))
            textbox.bind("<Button-3>", self.control_param_clicked)
            textbox.pack(expand=True)
            # Label at the bottom for the slot name
            label = tk.Label(frame, text=slot_name, bg="#555555", fg="white", font=("Arial", 10, "bold"))
            label.pack(side="bottom")

            return frame

        # Display Page 1 slots
        row_offset = 1  # Start after the close button
        for row in range(2):
            for col in range(3):
                num =1+(row)*3+col
                slot_text = f'param_{num}'
                slot_frame = create_slot(self.content_frame, slot_text, self.fx_parameters[slot_text])
                slot_frame.grid(row=row + row_offset, column=col, padx=15, pady=15)
                
        # Label for Page 1
        page1_label = tk.Label(self.content_frame, text="Page 1", bg="#333333", fg="white", font=("Arial", 12, "bold"))
        page1_label.grid(row=row_offset + 2, column=0, columnspan=3, pady=(20, 10))

        # Display Page 2 slots
        row_offset += 3  # Adjust the row offset for Page 2
        for row in range(2):
            for col in range(3):
                num =7+(row)*3+col
                slot_text = f'param_{num}'
                slot_frame = create_slot(self.content_frame, slot_text,self.fx_parameters[slot_text])
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
