import json
from tkinter.font import names

import requests

from main import get_config


def get_info(url: str, character: str):
    character = character.replace(" ", "%20")
    response = requests.get(url+f"?name={character}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data[0]['born']

if __name__ == '__main__':
    config = get_config()
    while True:
        name = input("Citeste un caracter: ")
        birth_year = get_info(config['url2'], character=name)
        print(f"Born in: {birth_year}")