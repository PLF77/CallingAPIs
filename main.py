import json
import requests
import urllib.parse

def get_random(category='any'):
    if category == 'any':
        response = requests.get('https://api.chucknorris.io/jokes/random')
    else:
        response = requests.get(f'https://api.chucknorris.io/jokes/random?categories={category}')

    return response.json()['value']

def search_text(text):
