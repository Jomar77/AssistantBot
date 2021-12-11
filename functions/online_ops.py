import requests
import pywhatkit as kit
from email.message import EmailMessage
from decouple import config


def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']