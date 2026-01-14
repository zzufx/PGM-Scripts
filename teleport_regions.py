import xml.etree.ElementTree as ET
import sys

def fix_xml_file(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        regions = {}

        for point in root.findall(".//point"):
            region_id = point.get("id")
            if region_id and point.text:
                coords = point.text.strip().split(",")
                if len(coords) == 3:
                    regions[region_id] = coords

        for cyl in root.findall(".//cylinder"):
            region_id = cyl.get("id")
            base = cyl.get("base")
            if region_id and base:
                coords = base.strip().split(",")
                if len(coords) == 3:
                    regions[region_id] = coords

        counter = 0
        for tp in root.findall(".//teleport"):
            region_id = tp.get("region")
            if region_id and region_id in regions:
                x, y, z = regions[region_id]
                tp.attrib.pop("region", None)
                tp.set("x", x)
                tp.set("y", y)
                tp.set("z", z)
                counter += 1

        if counter > 0:
            xml_str = ET.tostring(root, encoding="unicode", method="xml")
            xml_str = xml_str.replace(" />", "/>")
            xml_str = "\n".join([line for line in xml_str.splitlines() if line.strip()])
            with open(filename, "w", encoding="utf-8") as f:
                f.write(xml_str)
            print(f"Changed {counter} teleport(s) in {filename}")
        else:
            print(f"No teleports changed in {filename}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 teleport_regions.py <filename>")
    else:
        fix_xml_file(sys.argv[1])
