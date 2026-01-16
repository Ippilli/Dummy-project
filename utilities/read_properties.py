import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "..", "config.ini"))

def get_config(key):
    data = {
        "base_url": "https://www.saucedemo.com",
        "username": "standard_user",
        "password": "secret_sauce"
    }
    return data[key]