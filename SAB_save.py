import xml.etree.ElementTree as ET
from xml.dom import minidom

import tkinter as tk
from tkinter import filedialog


class SAB_save_load():
    def __init__(self,canvas,blocks,arrows,fx_parameters):
        self.canvas = canvas
        self.blocks = blocks
        self.arrows = arrows
        self.fx_parameters = fx_parameters
        self.root = ET.Element("SAB_code_gen_data")
    
    def save(self):
        print("save")
        # Need to save blocks 
        # 1.
        # save blocks
        # tag
        # values
        # position
        self.root.clear()
        outputs = []
        
        outputs.append(self.create_xml_from_blocks(self.blocks))

        # 2.
        # save arrows
        outputs.append(self.create_xml_from_arrows(self.arrows))
        
        # 3.
        # save parameters
        outputs.append(self.create_xml_from_fx_parameters(self.fx_parameters))

        self.save_here = filedialog.asksaveasfile(
            title="Save as...",
            defaultextension=".xml",  # Default extension
            filetypes=[("XML files", "*.xml"), ("All files", "*.*")],  # File types
            mode="w"  # Open in write mode
        )
        with open(self.save_here.name, "w", encoding="utf-8") as f:
            f.write(self.prettify_xml(self.root))
            # for output in outputs:
            #     f.write(self.prettify_xml(output))
 

    def load(self):
        print("load")
        self.open_here = filedialog.askopenfile(
            title="Open savefile",
            defaultextension=".xml",  # Default extension
            filetypes=[("XML files", "*.xml"), ("All files", "*.*")],  # File types
            mode="r"
        )
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()  # Get the root element

        # Process blocks, arrows, and fx_parameters
        blocks = root.find("blocks")
        arrows = root.find("arrows")
        fx_params = root.find("fx_parameters")

        return blocks,arrows,fx_params


    def create_xml_from_blocks(self,block_data):
        # Root element
        block_root = ET.SubElement(self.root, "blocks")

        # Loop through block data and create XML elements
        for block in block_data:
            # Create a block element
            x1,y1,x2,y2 = self.canvas.coords(block.tag)
            block_elem = ET.SubElement(block_root, "block", {
                "type": str(block.type),
                "tag": str(block.tag),
                "x": str(x1),
                "y": str(y1)
            })

            # # Add options if present
            try:
                opts_elem = ET.SubElement(block_elem, "option_vars")
                for opt in block.option_vars:
                    var_value = block.option_vars[opt].get('var').get()

                    ET.SubElement(opts_elem, opt, {
                    "var_value"        :str(var_value)
                })
            except:
                pass
            

        return block_root
    
    def create_xml_from_arrows(self,arrows):
        # Create root for arrows
        arrows_root = ET.SubElement(self.root, "arrows")

        # Add arrows
        for arrow in arrows:
            ET.SubElement(arrows_root, "arrow", {
                "src_out_id"        :str(arrow[0]),
                "dst_in_id"         :str(arrow[1]),
                "arrow_id"          :str(arrow[2]),
                "dst_block_tag"     :str(arrow[3]),
                "src_block_tag"     :str(arrow[4])
            })
        return arrows_root
    
    def create_xml_from_fx_parameters(self,fx_parameters):
        # Create root for arrows
        fx_parameters_root = ET.SubElement(self.root, "fx_parameters")

        # Add arrows
        for fx_parameter in fx_parameters.items():
            fx_param = ET.SubElement(fx_parameters_root, fx_parameter[0],{
                "assigned_block_tag"        :str(fx_parameter[1]['assigned_block_tag']),
                "assigned_block_setting"    :str(fx_parameter[1]['assigned_block_setting'])
            })
            setting_xml = ET.SubElement(fx_param, "settings")
            settings = fx_parameter[1]['settings']
            for setting in settings.items():
                ET.SubElement(setting_xml, "settings",{str(setting[0]):str(setting[1].get())})
                
            

        return fx_parameters_root
    
    def prettify_xml(self, elem):
        """Return a pretty-printed XML string for the Element."""
        rough_string = ET.tostring(elem, encoding="utf-8")
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")




# Write the XML to a file

# Load XML data from a file
def parse_xml(file_path):
    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()  # Get the root element

        # Process blocks, arrows, and fx_parameters
        blocks = process_blocks(root.find("blocks"))
        arrows = process_arrows(root.find("arrows"))
        fx_params = process_fx_parameters(root.find("fx_parameters"))
        
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except FileNotFoundError:
        print("File not found.")

# Process <blocks> section
def process_blocks(blocks):
    if blocks is not None:
        print("Blocks found:")
        for block in blocks:
            print(f"  Block: {block.tag}, Attributes: {block.attrib}")
    else:
        print("No blocks found.")

# Process <arrows> section
def process_arrows(arrows):
    if arrows is not None:
        print("Arrows found:")
        for arrow in arrows:
            print(f"  Arrow: {arrow.tag}, Attributes: {arrow.attrib}")
    else:
        print("No arrows found.")

# Process <fx_parameters> section
def process_fx_parameters(fx_parameters):
    if fx_parameters is not None:
        print("FX Parameters found:")
        for param in fx_parameters:
            print(f"  Param: {param.tag}, Attributes: {param.attrib}")
            settings = param.find("settings")
            if settings is not None:
                for setting in settings:
                    print(f"    Setting: {setting.tag}, Attributes: {setting.attrib}")
    else:
        print("No FX Parameters found.")

# Example usage
file_path = "blocks.xml"  # Replace with your XML file's path
parse_xml(file_path)

