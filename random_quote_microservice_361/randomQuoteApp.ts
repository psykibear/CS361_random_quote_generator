/**
 * @param backendPort The port number of the backend server.
 * @returns A string containing the random number.
 */

// For the Promises API
import { promises as fsPromises } from 'fs';

/**
 * @returns A string containing the random quote.
 */

async function fetchRandomQuote() {
  try {
    const data = await fsPromises.readFile('quotes.json', 'utf8');
    const quotes = JSON.parse(data).quotes;
    if (quotes.length === 0) throw new Error('No quotes found in the file.');
    const randomIndex = Math.floor(Math.random() * quotes.length);
    return `Here is your quote: "${quotes[randomIndex]}"`;
  } catch (error) {
    console.error("Error:", error);
  }
}

fetchRandomQuote()
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
