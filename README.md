# Microservice for a Random Quote Generator using an internal number generator. 
Please follow the instructions below to run, and how to make calls for this random quote generator microservice

## Background
This microservice implements a RESTful API to allow clients to send requests and receive responses in JSON format. The client can request and recieve randomly generated quotes. The random number is generated with a range that is based on the number of quotes in the JSON quote file.

## Prerequisites

- Node.js

## Installation

Follow the instructions below for setting up the project using windows commands:

1. Clone the repository:
    ```cmd
    git clone [https://github.com/](https://github.com/psykibear/CS361_random_quote_generator/tree/main/random_quote_microservice_361)
    ```
2. Install dependencies:
    ```cmd
    npm install
    ```
4. Start the server:
    ```cmd
    npm start
    ```

## Running the Sample Application
Run this sample application to make sure you are setup correctly and to observe an example of how to make calls. 

>**Note:** Make sure the server is running in parallel before running the program.

Run this command from the command line from the root of the folder.
```bash
ts-node randomQuoteApp.ts
```    
You should see output to the command line like the following:
```bash
Hello, here is your random Quote: ???
```
## API Reference
Ideally, this would be running via webserver, BUT for the purposes of this course and assignment it will be ran locally.

### Request
The following is how to make a call to the microservice:

**Random Quote:** Supply a single Quote.
```
http://localhost:<Your backend port here>/api/random
```

**Example:** The given call below will generate a Quote, assuming the port is 3050.
```
http://localhost:3050/api/random/
```

### Response
All calls shall return the data in JSON format as shown:

```json
{
    "randomQuote": <Quote>
}
```
## UML Sequence Diagram
Below is an example of a sequence of a call for the random Quote
![Random Quote Generator UML](UML.PNG)
