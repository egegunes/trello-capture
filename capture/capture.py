try:
    import configparser
except ImportError:
    import ConfigParser as configparser

import os
import sys

import requests


url = "https://api.trello.com/1/cards"


def run():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.getenv("HOME"), ".trello"))

    try:
        key = config["trello"]["key"]
        token = config["trello"]["token"]
        listID = config["trello"]["listID"]
    except AttributeError:
        key = config.get("trello", "key")
        token = config.get("trello", "token")
        listID = config.get("trello", "listID")

    if len(sys.argv) < 2:
        print("Card content is required")
        sys.exit(1)

    querystring = {
        "name": " ".join(sys.argv[1:]),
        "idList": listID,
        "key": key,
        "token": token
    }

    try:
        response = requests.post(url, params=querystring)
        response.raise_for_status()
    except requests.HTTPError as e:
        print("Error: {}".format(e))
