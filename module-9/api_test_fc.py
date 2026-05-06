"""
api_test_fc.py
Author: Fernando Contreras
Assignment: CSD-325 Module 9
Description: Tests connection to a URL using the requests library.
             Part 1 of the API tutorial — verifying the requests module works.
"""

import requests

# Test connection to Open Notify API
url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
print(response.status_code)
