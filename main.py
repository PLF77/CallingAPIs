import json
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/random", methods=["GET"])
def get_random():
    category = request.args.get('cat', '')
    if category == '':
        response = requests.get('https://api.chucknorris.io/jokes/random')
        return response.json()['value']
    elif category not in requests.get('https://api.chucknorris.io/jokes/categories').json():
        raise ValueError('Wrong category...')
    else:
        response = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')
        return response.json()['value']


@app.route("/cat", methods=["GET"])
def cat():
    str = 'Available categories: '
    cat = requests.get('https://api.chucknorris.io/jokes/categories').json()
    for i in range(0, len(cat)):
        if i == len(cat)-1:
            str += cat[i]
        else:
            str += cat[i] + ', '

    return str


if __name__ == '__main__':
    app.run(debug=True)

