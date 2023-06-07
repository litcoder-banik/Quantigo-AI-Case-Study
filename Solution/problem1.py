import json
import os

def convert_format(input_path, output_path):
    with open(input_path, 'r') as file:
        data = json.load(file)

    formatted_data = [
        {
            "dataset_name": os.path.basename(input_path),
            "image_link": "",
            "annotation_type": "image",
            "annotation_objects": {
                "vehicle": {
                    "presence": 0,
                    "bbox": []
                },
                "license_plate": {
                    "presence": 0,
                    "bbox": []
                }
            },
            "annotation_attributes": {
                "vehicle": {
                    "Type": None,
                    "Pose": None,
                    "Model": None,
                    "Make": None,
                    "Color": None
                },
                "license_plate": {
                    "Difficulty Score": None,
                    "Value": None,
                    "Occlusion": None
                }
            }
        }
    ]

    if "objects" in data:
        for obj in data["objects"]:
            class_title = obj.get("classTitle")
            tags = obj.get("tags", [])
            bbox = obj.get("points", {}).get("exterior", [])

            if class_title == "Vehicle":
                formatted_data[0]["annotation_objects"]["vehicle"]["presence"] = 1
                formatted_data[0]["annotation_objects"]["vehicle"]["bbox"] = bbox

                for tag in tags:
                    name = tag.get("name")
                    value = tag.get("value")

                    if name in formatted_data[0]["annotation_attributes"]["vehicle"]:
                        formatted_data[0]["annotation_attributes"]["vehicle"][name] = value

            elif class_title == "License Plate":
                formatted_data[0]["annotation_objects"]["license_plate"]["presence"] = 1
                formatted_data[0]["annotation_objects"]["license_plate"]["bbox"] = bbox

                for tag in tags:
                    name = tag.get("name")
                    value = tag.get("value")

                    if name in formatted_data[0]["annotation_attributes"]["license_plate"]:
                        formatted_data[0]["annotation_attributes"]["license_plate"][name] = value

    with open(output_path, 'w') as file:
        json.dump(formatted_data, file, indent=4)

# Example usage:
input_path = r"E:\CaseStudy\json_files\pos_0.png.json"
output_path = r"E:\CaseStudy\json_files_formatted\Solution_formatted_pos_0.png.json"
convert_format(input_path, output_path)
