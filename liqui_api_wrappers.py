import requests
import json

def get_info():
    url = 'https://api.liqui.io/api/3/info'
    data = None
    response = requests.get(url)
    return response.json()



