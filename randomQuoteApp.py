import json

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {"error": "File not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}

# Example Usage
file_path = 'randomQuote.json'
json_data = load_json_file(file_path)
print(json_data)