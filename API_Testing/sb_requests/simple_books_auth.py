import requests as req
import random

# Construim metoda get token pentru a recupera un token de auth pt interactiunea cu API simple books.

URL = "https://simple-books-api.glitch.me/api-clients/"

def get_token():
    number = random.randint(1,999)
    data = {
        "clientName": "Postman",
        "clientEmail": f"george{number}@example.com"
    }
    response = req.post(URL, json=data)
    #print(response.json()["accessToken"])
    return response.json()["accessToken"]

#get_token()
#print(get_token())
