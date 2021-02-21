import base64
import json
import requests
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/random", methods=["GET"])
def get_random():
    category = request.args.get('cat', '')
    if category == '':
        response = requests.get('https://api.chucknorris.io/jokes/random')
        return response.json()['value']
    elif category not in requests.get('https://api.chucknorris.io/jokes/categories').json():
        return code_status()
    else:
        response = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')
        return response.json()['value']


@app.route("/cat", methods=["GET"])
def cat():
    str = 'Available categories: '
    cat = requests.get('https://api.chucknorris.io/jokes/categories').json()
    if not requests.get('https://api.chucknorris.io/jokes/categories'):
        return code_status()
    for i in range(0, len(cat)):
        if i == len(cat)-1:
            str += cat[i]
        else:
            str += cat[i] + ', '
    return str

def code_status():
    return render_template("cats.html")


if __name__ == '__main__':
    app.run(debug=True)

