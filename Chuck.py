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
    for i in cat:
        str += i + ', '
    return str


if __name__ == '__main__':
    app.run(debug=True)

# def split_command(command):
#     """
#     split command into command word and command parameters
#     :param command: initial command
#     :return: command word and command parameters in list
#     """
#     command = command.strip()
#     tokens = command.split(' ', 1)
#     command_word = tokens[0].strip().lower()
#     command_params = tokens[1].strip() if len(tokens) == 2 else ''
#     return command_word, command_params
#
# def options():
#     print('>chuck')
#     print('>chuck <category>')
#     print('>cat')
#
#
# def start_command_ui():
#     command_dict = {'chuck': get_random, 'cat': cat}
#     done = False
#     options()
#     while not done:
#         command = input('command> ')
#         try:
#             # split into command_word and command_params
#             cmd_word, cmd_params = split_command(command)
#             # have separate functions for each command word
#             if cmd_word in command_dict:
#                 command_dict[cmd_word](cmd_params)
#             elif cmd_word == 'exit':
#                 done = True
#             else:
#                 print('bad command')
#         except ValueError as ve:
#             print(str(ve))
#
#
# #start_command_ui()
