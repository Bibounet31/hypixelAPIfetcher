import requests
import json

# ahem, super secret key (hypixel api)
key = { "API-Key": "8c21f916-d0c8-44f6-94d2-72cfdc888f62" }



# ask player username
name = str(input("please enter ur minecraft name: "))

# add username to link, then fetching with that address to mojang's api 
print("waiting for mojang's reply..")
response = requests.get("https://api.mojang.com/users/profiles/minecraft/"+ name)

# mojangs returns crap, take only the id
playerUID = response.json()["id"]

# adding playerUID into a dict cuz thats how u send params to an api ig
playerid = {"uuid" : playerUID}

#api request to hypixel
print("waiting for hypixel's reply...")
response = requests.get("https://api.hypixel.net/v2/player", headers=key, params=playerid)

# writting result in a json file uwu
print("writting result to file....")
with open("data.json", "w") as f:
    json.dump(response.json(), f)

print("done!")







