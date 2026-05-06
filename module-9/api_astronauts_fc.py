"""
api_astronauts_fc.py
Author: Fernando Contreras
Assignment: CSD-325 Module 9
"""

import requests

# ── Part 1: Test connection ───────────────────────────────────────────
print("--- Connection Test ---")
response = requests.get('http://api.open-notify.org/astros.json')
print(f"Status code: {response.status_code}")
print()

# ── Part 2: Retrieve and format astronaut data ────────────────────────
print("--- Current Astronauts in Space ---")

# Parse the JSON response
data = response.json()

# Print total number of people in space
print(f"Number of people in space: {data['number']}")
print()

# Loop through each astronaut and format output
for astronaut in data['people']:
    print(f"Name: {astronaut['name']}")
    print(f"Craft: {astronaut['craft']}")
    print("---")
