# Microservice for a Random Quote Generator.
Please follow the instructions below to run, and how to make calls for this random quote generator microservice

## Background
This microservice implements a python function to allow clients to send requests and receive responses in JSON format. The client can request and recieve randomly generated quotes. The random number is generated with a range that is based on the number of quotes in the JSON quote file.

## Prerequisites

Python3

## Installation

Follow the instructions below for setting up the project using commands:

1. npm install Python3

## Running the Sample Application
Run this sample application to make sure you are setup correctly and to observe an example of how to make calls. 

Make sure the microservice is running in the background
python3 randomQuote.py

In a new terminal window run the following:
python3 randomQuoteApp.py
The terminal then should print the quote in the terminal based on the sample app. 

### Response
All calls shall return the data in JSON format as shown:

```json
[
    <quote>
]
```
## UML Sequence Diagram
See the UML.PNG file for the sequence diagram.
