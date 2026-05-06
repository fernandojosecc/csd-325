"""
api_main_fc.py
Author: Fernando Contreras
Assignment: CSD-325 Module 9
Description: Uses the JokeAPI (https://v2.jokeapi.dev) to retrieve jokes.
             Tests the connection, prints the raw response, then prints

API chosen: JokeAPI — free, returns JSON data.
URL: https://v2.jokeapi.dev/joke/Programming?amount=3
"""

import requests
import json

API_URL = 'https://v2.jokeapi.dev/joke/Programming?amount=3'

# ── Step 1: Test the connection ───────────────────────────────────────
print("--- Connection Test ---")
response = requests.get(API_URL)
print(f"Status code: {response.status_code}")
print()

# ── Step 2: Print raw (unformatted) response ──────────────────────────
print("--- Raw Response ---")
print(response.text)
print()

# ── Step 3: Print formatted response ─────────────────────────────────
print("--- Formatted Response ---")
data = response.json()

jokes = data['jokes']
print(f"Number of jokes retrieved: {len(jokes)}")
print()

for i, joke in enumerate(jokes, start=1):
    print(f"Joke {i}:")
    print(f"  Category : {joke['category']}")
    if joke['type'] == 'single':
        print(f"  Joke     : {joke['joke']}")
    else:
        print(f"  Setup    : {joke['setup']}")
        print(f"  Delivery : {joke['delivery']}")
    print()
