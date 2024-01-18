# Star Wars Characters Script

This script is designed to retrieve and display all the characters from a specific Star Wars movie using the Star Wars API. The user needs to provide the Movie ID as a positional argument, and the script will fetch the relevant information from the API, displaying one character name per line in the same order as the characters appear in the `/films/` endpoint.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

- Python: The script is written in Python, so ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

- Requests Module: The script uses the `requests` module to interact with the Star Wars API. If you don't have it installed, you can install it using:

```bash
pip install requests
```

## Usage

To run the script, execute the following command in your terminal:

```bash
python star_wars_characters.py <Movie_ID>
```

Replace `<Movie_ID>` with the desired Movie ID. For example, to get characters from "Return of the Jedi," use:

```bash
python star_wars_characters.py 3
```

## Script Description

The script utilizes the Star Wars API to fetch information about a specific movie and extracts the list of characters from the `/films/` endpoint. It then prints the character names one per line in the same order as they appear in the API response.

## Example

```bash
python star_wars_characters.py 3
```

Output:

```
Luke Skywalker
Han Solo
Princess Leia Organa
...
```

## Error Handling

The script includes basic error handling to ensure a smooth execution. It checks for valid Movie IDs and handles potential connection issues with the Star Wars API.

Feel free to explore and modify the script as needed for your specific use case!
