from pypresence import Presence
import time
from infojtoh import *


client_id = "922861689207132220"
RPC = Presence(client_id)
RPC.connect()


data = dict(
    state="Ring Select",
    large_image="ring",
    large_text="Ring Select",
)


while True:
    RPC.update(**data)


    command = input().split()

# Basic Commands

    if command[0] == "tower":
        if len(command) > 1:
            data["state"] = f"{' '.join(command[1:])}"
            print(f'Set Tower to: "{" ".join(command[1:])}"')
        elif "state" in data:
            data.pop("state")

    elif command[0] == "difficulty" or command[0] == "diff":
        if len(command) > 1:
            data["small_text"] = f"{' '.join(command[1:])}"
            print(f'Set difficulty text to: "{" ".join(command[1:])}"')
        elif "small_image" in data:
            data.pop("small_image")

    elif command[0] == "info" or command[0] == "state" or command[0] == "details":
        if len(command) > 1:
            data["details"] = f"{' '.join(command[1:])}"
            print(f'Set details to: "{" ".join(command[1:])}"')
        elif "details" in data:
            data.pop("details")

    elif command[0] == "time":
        if "start" in data:
            data.pop("start")
    
    elif command[0] == "boss":
        data["state"] = "boss time"
    
    elif command[0] == "lobby":
        data["state"] = "Exploring"


# Useful Stuff
    
    elif command[0].isdecimal():
        data["start"] = int(time.time()) - int(command[0])
    
    elif command[0] == "t":
        data["state"] = f"Tower of {' '.join(command[1:])}"

    elif command[0] == "c":
        data["state"] = f"Citadel of {' '.join(command[1:])}".title()
    
    elif command[0] == "s":
        data["state"] = f"Steeple of {' '.join(command[1:])}".title()
    
    elif command[-1] in Difficulties:
        data["small_image"] = Difficulties[command[-1]]
        data["small_text"] = f'{" ".join(command[:-1])} {Difficulties[command[-1]].title()}'

    elif command[0] in Realms:
        realm = Realms[command[0]]
        data["large_image"] = realm[1]
        data["large_text"] = realm[0]

    else:
        print("what")
