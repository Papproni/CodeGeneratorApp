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
def prettify_xml(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, encoding="utf-8")
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# Convert block data to XML
def create_xml_from_blocks(block_data):
    # Root element
    root = ET.Element("blocks")

    # Loop through block data and create XML elements
    for block in block_data:
        # Create a block element
        block_elem = ET.SubElement(root, "block", {
            "type": block["type"],
            "tag": block["tag"],
            "x": block["x"],
            "y": block["y"]
        })

        # Add options if present
        if "opts" in block:
            opts_elem = ET.SubElement(block_elem, "options")
            for key, value in block["opts"].items():
                ET.SubElement(opts_elem, key).text = value

    return root

# Generate the XML
root = create_xml_from_blocks(block_data)

# Pretty-print the XML
pretty_xml = prettify_xml(root)

# Write the XML to a file
with open("blocks.xml", "w", encoding="utf-8") as f:
    f.write(pretty_xml)

print("XML file 'blocks.xml' created successfully!")