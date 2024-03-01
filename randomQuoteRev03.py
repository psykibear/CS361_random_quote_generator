import time
import random
import json
import os

def load_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {"error": "File not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}

while True:
    time.sleep(5)
    # Verify that the JSON file exists
    if os.path.exists("quoteList.json"):
        # Load the JSON file
        json_data = load_json_file("quoteList.json")
        # Check if the loaded data is a dictionary
        if isinstance(json_data, dict) and "quotes" in json_data:
            quotes = json_data["quotes"]
            if quotes:
                # Select a random quote from the list of quotes
                random_quote = random.choice(quotes)
                #if the randomQuote.json file exists and is empty
                if os.path.exists("randomQuote.json") and os.path.getsize("randomQuote.json") == 0:
                    # Write the selected quote to a new JSON file
                    with open("randomQuote.json", "w") as output_file:
                        json.dump({"quote": random_quote}, output_file, indent=4)
            else:
                print("The JSON file does not contain a valid list of quotes.")
        else:
            print("The JSON file does not contain a valid dictionary with 'quotes' key.")
    else:
        print("The quoteList.json file does not exist.")
