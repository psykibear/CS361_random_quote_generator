from flask import Flask, jsonify, request
import json
import random
import os

app = Flask(__name__)
quotes_file_path = 'quoteList.json'

def load_json_file(file_path):
    """Loads and returns the content of the JSON file."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_json_file(file_path, data):
    """Saves data to the JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/quotes', methods=['GET', 'POST'])
def manage_quotes():
    quotes = load_json_file(quotes_file_path)
    if request.method == 'GET':
        if not quotes:
            return jsonify({"error": "No quotes found"}), 404
        return jsonify(quotes)
    elif request.method == 'POST':
        new_quote = request.json
        quotes.append(new_quote)
        save_json_file(quotes_file_path, quotes)
        return jsonify(new_quote), 201

@app.route('/quotes/<int:index>', methods=['GET', 'PUT', 'DELETE'])
def handle_quote(index):
    quotes = load_json_file(quotes_file_path)
    if request.method == 'GET':
        try:
            return jsonify(quotes[index])
        except IndexError:
            return jsonify({"error": "Quote not found"}), 404
    elif request.method == 'PUT':
        try:
            quotes[index] = request.json
            save_json_file(quotes_file_path, quotes)
            return jsonify(quotes[index])
        except IndexError:
            return jsonify({"error": "Quote not found"}), 404
    elif request.method == 'DELETE':
        try:
            removed_quote = quotes.pop(index)
            save_json_file(quotes_file_path, quotes)
            return jsonify(removed_quote)
        except IndexError:
            return jsonify({"error": "Quote not found"}), 404

@app.route('/random-quote', methods=['GET'])
def random_quote():
    quotes = load_json_file(quotes_file_path)
    if not quotes:
        return jsonify({"error": "No quotes found"}), 404
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
