import xml.etree.ElementTree as ET
from xml.dom import minidom


# Data to populate the XML
block_data = [
    {
        "type": "Biquad_filter",
        "tag": "block1",
        "x": "100",
        "y": "100",
        "opts": {
            "Freq": "Param1",
            "Q":    "0.707"
        }

    },
    {
        "type": "INPUT_BLOCK",
        "tag": "block2",
        "x": "50",
        "y": "50"
    },
    {
        "type": "OUTPUT_BLOCK",
        "tag": "block3",
        "x": "150",
        "y": "50"
    }
]
# Function to pretty-print the XML


# Convert block data to XML


class SAB_save_load():
    def __init__(self,canvas,blocks,arrows,fx_parameters):
        self.canvas = canvas
        self.blocks = blocks
        self.arrows = arrows
        self.fx_parameters = fx_parameters
    
    def save(self):
        print("save")
        # Need to save blocks 
        # 1.
        # save blocks
        # tag
        # values
        # position
        outputs = []
        
        outputs.append(self.create_xml_from_blocks(self.blocks))

        # 2.
        # save arrows
        outputs.append(self.create_xml_from_arrows(self.arrows))
        
        # 3.
        # save parameters
        outputs.append(self.create_xml_from_fx_parameters(self.fx_parameters))

        with open("blocks.xml", "w", encoding="utf-8") as f:
            for output in outputs:
                f.write(self.prettify_xml(output))
 

    def load(self):
        print("load")


    def create_xml_from_blocks(self,block_data):
        # Root element
        block_root = ET.Element("blocks")

        # Loop through block data and create XML elements
        for block in block_data:
            # Create a block element
            x1,y1,x2,y2 = self.canvas.coords(block.tag)
            block_elem = ET.SubElement(block_root, "block", {
                "type": block.type,
                "tag": block.tag,
                "x": x1,
                "y": y1
            })

            # Add options if present
            try:
                opts_elem = ET.SubElement(block_elem, "option_vars")
                for opt in block.option_vars:
                    var_value = block.option_vars[opt].get('var').get()

                    ET.SubElement(opts_elem, opt, {
                    "var_value"        :var_value
                })
                
                for key, value in block["opts"].items():
                    ET.SubElement(opts_elem, key).text = value
            except:
                pass
            

        return block_root
    
    def create_xml_from_arrows(self,arrows):
        # Create root for arrows
        arrows_root = ET.Element("arrows")

        # Add arrows
        for arrow in arrows:
            ET.SubElement(arrows_root, "arrow", {
                "src_out_id"        :arrow[0],
                "dst_in_id"         :arrow[1],
                "arrow_id"          :arrow[2],
                "dst_block_tag"     :arrow[3],
                "src_block_tag"     :arrow[4]
            })
        return arrows_root
    
    def create_xml_from_fx_parameters(self,fx_parameters):
        # Create root for arrows
        fx_parameters_root = ET.Element("fx_parameters")

        # Add arrows
        for fx_parameter in fx_parameters.items():
            settings = fx_parameter[1]['settings']
            fx_param = ET.SubElement(fx_parameters_root, fx_parameter[0], {
                "assigned_block_tag"        :fx_parameter[1]['assigned_block_tag'],
                "assigned_block_setting"    :fx_parameter[1]['assigned_block_setting']
            })
            setting_xml = ET.SubElement(fx_param, "settings")
            for setting in settings.items():
                ET.SubElement(setting_xml, "settings",{setting[0]:setting[1].get()})
                
            

        return fx_parameters_root
    
    def prettify_xml(self, elem):
        """Return a pretty-printed XML string for the Element."""
        rough_string = ET.tostring(elem, encoding="utf-8")
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")




# Write the XML to a file


print("XML file 'blocks.xml' created successfully!")