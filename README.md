# Microservice for a Random Quote Generator.
Please follow the instructions below to run, and how to make calls for this random quote generator microservice

## Background
This microservice implements a python function to allow clients to send requests and receive responses in JSON format. The client can request and recieve randomly generated quotes. The random number is generated with a range that is based on the number of quotes in the JSON quote file.

## Prerequisites

Python3

## Installation

Follow the instructions below for setting up the project using commands:
If you do not have python installed on your machine go to your terminal, 
and install the appropriate Python as described using the following command in your terminal window: npm install Python3

## Running the Sample Application
Run this sample application to make sure you are setup correctly and to observe an example of how to make calls. 

Open a new terminal window changing the directory to where the zip folder was downloaded and extracted. 

Start by running the the microservice in the background by running it in its own terminal window (or tab) using the following command:
python3 randomQuote.py
This microservice is how you REQUEST data. 

Open a new terminal window (or tab) and run the following command:
python3 randomQuoteApp.py
The sample app is how you RECEIVE data. 

This will run the sample app to then display the random quote that was sent to the JSON file through the microservice application running in the background.

### Response
All calls shall return the data in JSON format as shown:

```json
{

    "quote":<randomQuote>

}
```
## UML Sequence Diagram
See the UML.PNG file for the sequence diagram.
