import json

# Your original dictionary
original_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

# Convert the original dictionary into a list of dictionaries
list_of_dicts = [{"item": value} for key, value in original_dict.items()]

# Save each dictionary as a separate JSON file
for i, sub_dict in enumerate(list_of_dicts, 1):
    json_filename = f"output_{i}.json"
    
    with open(json_filename, "w") as json_file:
        json.dump(sub_dict, json_file, indent=2)

    print(f"JSON file {json_filename} created.")
