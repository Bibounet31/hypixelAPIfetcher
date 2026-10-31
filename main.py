import requests
import json

# ahem, super secret key (hypixel api)
key = { "API-Key": "urapikey" }


# ask player username
name = input("please enter ur minecraft name: ")



# add username to link, then fetching with that address to mojang's api 
print("waiting for mojang's reply..")
response = requests.get("https://api.mojang.com/users/profiles/minecraft/"+ name)
# checks
if response.status_code in (204, 404):
    raise ValueError("that player doesn't exist, typo?")
if response.status_code == 504:
    raise ValueError("Mojang's api Error, please try again")
response.raise_for_status()
# mojangs returns crap, take only the id
try:    
    playerUID = response.json()["id"]
except (ValueError, KeyError, TypeError):
    raise ValueError("seems like there's something wrong with mojang's reply! please try again") from None



# adding playerUID into a dict cuz thats how u send params to an api ig
playerid = {"uuid" : playerUID}

#api request to hypixel
print("waiting for hypixel's reply...")
response = requests.get("https://api.hypixel.net/v2/player", headers=key, params=playerid)

# writing result in a json file uwu
print("writing result to file....")
with open("data.json", "w") as f:
    json.dump(response.json(), f)

print("done!")







