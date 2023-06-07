import os
import json

def combine_files(path):
    data = []

    for file_name in os.listdir(path):
        if file_name.endswith(".json"):
            file_path = os.path.join(path, file_name)
            
            with open(file_path, "r") as file:
                json_data = json.load(file)
            
            for obj in json_data["objects"]:
                if obj["classTitle"] == "Vehicle":
                    obj["classTitle"] = "Car"
                elif obj["classTitle"] == "License Plate":
                    obj["classTitle"] = "Number"
            
            data.extend(json_data["objects"])
    
    combined_json = {
        "objects": data
    }
    
    output_file = "Solution_combined.json"
    output_path = os.path.join(path, output_file)
    with open(output_path, "w") as file:
        json.dump(combined_json, file, indent=4)
    
    print("Combined JSON file created:", output_file)

path = r"E:\CaseStudy\json_files"

combine_files(path)
