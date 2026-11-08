# imports
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


# ahem, super secret key (hypixel api)
key = os.getenv('Hypixel_API_Key')



def GetMojangUUIDFromName(name):
    """Get user UUID using mojang API system"""
    
    # add username to link, then fetching with that address to mojang's api 
    print("waiting for mojang's reply..")
    response = requests.get("https://api.mojang.com/users/profiles/minecraft/"+ name)
    
    # mojangs returns crap, take only the id
    try:    
        playerUID = response.json()["id"]
    except (ValueError, KeyError, TypeError):
        raise ValueError("seems like there's something wrong with mojang's reply! please try again") from None


    # adding playerUID into a dict cuz thats how u send params to an api ig
    playerid = {"uuid" : playerUID}

    return playerid




def GetPlayerStats(key,name):
    """api request to hypixel"""
    print("waiting for hypixel's reply...")
    #response = requests.get("https://api.hypixel.net/v2/status", headers=key, params=playerid)

    response = requests.get("https://api.hypixel.net/v2/player", headers={"API-Key":key}, params=GetMojangUUIDFromName(name))

    #response = requests.get("https://api.hypixel.net/v2/recentgames", headers=key, params=playerid)
    return response


def WriteIntoFile(name):
    # writing result in a json file uwu
    print("writing result to file....")
    with open("data.json", "w") as f:
        json.dump(GetPlayerStats(key,name).json(), f)

    print("writting into file done!")




def main():
    # ask player username
    name = input("please enter ur minecraft name: ")

    WriteIntoFile(name)



main()