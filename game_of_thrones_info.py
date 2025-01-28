import json
import requests
from requests.exceptions import MissingSchema
from main import get_config


def get_lord_info(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        response_data = json.loads(response.text)
        return response_data['name']


def get_house_info(url: str):
        response = requests.get(url)
        if response.status_code == 200:
            response_data = json.loads(response.text)
            for elem in response_data:
                try:
                    house = elem['name']
                    lord = get_lord_info(elem['currentLord'])
                    print(f"{house} - {lord}")
                except MissingSchema as e:
                    print(f"{house} - unknown")


def get_books_info(url: str, year: int):
    response = requests.get(url)
    if response.status_code == 200:
        response_data = json.loads(response.text)
        for elem in response_data:
            rel_year = elem['released']
            name = elem['name']
            if int(rel_year[0:4]) >= year:
                print(name)


if __name__ == '__main__':
    config = get_config()
    print("\nGame of Thrones houses:\n")
    get_house_info(config['url3'])
    user_choice = int(input("\nYear: "))
    print(f"\nBooks published after {user_choice}:\n")
    get_books_info(config['url4'], year = user_choice)