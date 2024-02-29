import time
import random
import json
import os

while True:
    time.sleep(5)
    # Verify that the JSON file exists
    if os.path.exists("quoteList.json"):
        try:
            # Attempt to open and load the JSON file to check for validity
            with open("quoteList.json", "r") as json_file:
                data = json.load(json_file)
                # Ensure the data is in the expected format, e.g., a list
                if isinstance(data, list) and data:
                    # Select a random quote from the JSON data
                    random_quote = random.choice(data)
                    # Write the selected quote to a new JSON file
                    with open("randomQuote.json", "w") as output_file:
                        json.dump(random_quote, output_file, indent=4)
                else:
                    print("The JSON file does not contain a valid list of quotes.")
        except json.JSONDecodeError:
            print("The JSON file is not valid.")
    else:
        print("The quoteList.json file does not exist.")

