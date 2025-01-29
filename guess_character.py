import json
import time

import requests
from main import get_config


def get_char(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        response_data = json.loads(response.text)
    return response_data


def guess_char():
    counter = 0
    while True:
        try:
            user_choice = int(input("Enter a number between 1 and 999: "))
            if user_choice < 1 or user_choice > 999:
                print("Number must be between 1 and 999.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        config = get_config()
        character = get_char(config['url2'] + f"/{user_choice}")

        aliases = character.get("aliases")
        titles = character.get("titles")
        name = character.get("name")

        if len(name) > 0 and len(aliases) > 0:
            print(f"Alias: {aliases}")
        elif len(titles) > 0:
            print(f"Title: {titles}")
        else:
            print("Enter another number.")
            continue

        user_guess = input("Guess character name: ")
        if user_guess.lower() == name.lower():
            print("Corect!")
            counter += 1
        else:
            print("Wrong!")

        continue_game = input("Do you wish to continue? (Y/N): ")
        if continue_game.lower() != "Y":
            break

        game_data = {
            "timestamp": int(time.time()),
            "characters_guessed": counter
        }

        with open("game.json", "w") as f:
            json.dump(game_data, f, indent=4)


if __name__ == '__main__':
    guess_char()