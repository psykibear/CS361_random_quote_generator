from flask import Flask, jsonify, send_file
import json
import random

app = Flask(__name__)

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            quote = json.load(file)
            return quote
    except FileNotFoundError:
        return {"error": "File not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}

def get_random_entry(quote):
    if isinstance(quote, list):
        return random.choice(quote)
    elif isinstance(quote, dict):
        return random.choice(list(quote.items()))
    return {"error": "Invalid quote format"}

def create_new_json_file(file_path, quote):
    with open(file_path, 'w') as file:
        json.dump(quote, file, indent=4)
        return file_path

@app.route('/random-entry', methods=['GET'])
def random_entry():
    input_file_path = 'quoteList.json'
    output_file_path = 'randomQuote.json'

    json_data = load_json_file(input_file_path)
    random_entry = get_random_entry(json_data)
    output_file_path = create_new_json_file(output_file_path, random_entry)

    return send_file(output_file_path, mimetype='application/json')

if __name__ == '__main__':
    app.run(port=5000, debug=True)