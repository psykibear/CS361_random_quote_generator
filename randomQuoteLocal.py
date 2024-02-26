import json
import random

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {"error": "File not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}

def get_random_entry(data):
    if isinstance(data, list):
        return random.choice(data)
    elif isinstance(data, dict):
        return random.choice(list(data.items()))
    return {"error": "Invalid data format"}

def create_new_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    input_file_path = 'data.json'
    output_file_path = 'random_data.json'

    json_data = load_json_file(input_file_path)
    random_entry = get_random_entry(json_data)
    create_new_json_file(output_file_path, random_entry)