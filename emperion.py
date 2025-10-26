import time
import json
import os
import random

SAVE_FILE = "save.json"

if not os.path.exists(SAVE_FILE):
    print("creating save")
    save_data = {
        "name": None,
        "kingdom": None,
        "economy": 0,
        "progress": {},
        "character_created": False,
        "player_economy": 25,
        "blackspire_economy": 90,
        "player_territory": 5,
        "blackspire_territory": 15,
        "total_tiles": 20,
        "active_laws": [],
        "last_formation": None
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(save_data, f, indent=4)
else:
    print("loading save")
    with open(SAVE_FILE, "r") as f:
        save_data = json.load(f)

LAWS = {
    "Tax Relief Act": {"economy": +5},
    "Mandatory Conscription": {"economy": -3, "troops": +2},
    "Trade Embargo": {"blackspire_economy": -4},
    "Cultural Reinvestment": {"economy": +2, "morale": +3},
    "Emergency War Powers": {"morale": -2, "troops": +3}
}

FORMATIONS = ["V", "_", "^"]
ROWS, COLS = 4, 5
SEASONS = ["Spring", "Summer", "Autumn", "Winter"]

def determine_battle(player_choice, enemy_choice):
    if player_choice == enemy_choice:
        return "draw"
    elif ((player_choice == "^" and enemy_choice == "V") or
          (player_choice == "V" and enemy_choice == "_") or
          (player_choice == "_" and enemy_choice == "^")):
        return "victory"
    else:
        return "defeat"

def get_kingdom_symbol(name):
    first = name.strip()[0].upper()
    if first == "B":
        return name[1].upper() if len(name) > 1 else "P"
    return first

def generate_map(player_territory, blackspire_territory, rows=ROWS, cols=COLS, player_symbol=None, enemy_symbol='B'):
    all_tiles = [player_symbol]*player_territory + [enemy_symbol]*blackspire_territory
    all_tiles += ['N'] * (rows*cols - len(all_tiles))
    map_grid = []
    for r in range(rows):
        row = all_tiles[r*cols:(r+1)*cols]
        map_grid.append(row)
    return map_grid

def display_map(map_grid):
    print("MAP OF EMPERION")
    print(" " + "_ " * COLS)
    for row in map_grid:
        print("|" + "|".join(row) + "|")
    print(" " + "‾ " * COLS)

if not save_data["character_created"]:
    name = input("Greeting my fair king! what shall I call you!: ").capitalize()
    save_data["name"] = name
    print(f"Well hello King {name}, I am the Court Jester!")
    time.sleep(1)
    kingdom = input(f"Now King {name}, excuse my absentmindedness but what was the name of our kingdom again?:").capitalize()
    save_data["kingdom"] = kingdom
    print(f"Oh yes! how could I forget the glorious kingdom of {kingdom}!")
    time.sleep(1)
    first_invalid = True
    while True:
        irrelevent_q1 = input("Are you familiar with the state of the nation? Y or N").upper()
        if irrelevent_q1 == "Y":
            print(f"Perfect! then no time will be wasted King {name}!")
            break
        elif irrelevent_q1 == "N":
            print("Now from what I have heard,")
            time.sleep(2)
            print("please do excuse me if I am wrong, no one really takes a silly old Court Jester too seriously.")
            time.sleep(3)
            print("Your brother was a tad bit egotistical, and he left our fine kingdom in extreme disarray.")
            time.sleep(3)
            print("He started his term by starting war with the biggest baddest kingdom on the block, Blackspire.")
            time.sleep(3)
            print("And then the cherry on top! he introduced crazy taxes, 48.65%!")
            time.sleep(3)
            print("If you didn't want to pay those taxes, you had to join the military. Which was certain death, Blackspire was ruthless!")
            time.sleep(6)
            break
        else:
            if first_invalid:
                print("Y or N")
                first_invalid = False
    save_data["character_created"] = True
    with open(SAVE_FILE, "w") as f:
        json.dump(save_data, f, indent=4)
else:
    print(f"Welcome back, King {save_data['name']} of {save_data['kingdom']}!")

player_symbol = get_kingdom_symbol(save_data["kingdom"])
save_data["map"] = generate_map(save_data["player_territory"], save_data["blackspire_territory"], player_symbol=player_symbol)
display_map(save_data["map"])

current_turn = 1
while True:
    current_season = SEASONS[(current_turn-1) % 4]
    print(f"{current_season.upper()} - Turn {current_turn}")
    display_map(save_data["map"])

    print("LEGISLATION PHASE")
    available_laws = [law for law in LAWS if law not in save_data["active_laws"]]
    laws_to_pass = random.sample(available_laws, min(3, len(available_laws)))
    laws_to_revoke = random.sample(save_data["active_laws"], min(3, len(save_data["active_laws"]))) if save_data["active_laws"] else []

    print("Laws you can pass:", laws_to_pass)
    print("Laws you can revoke:", laws_to_revoke)
    choice = input("Type a law to pass/revoke or enter to skip: ")
    if choice in laws_to_pass:
        save_data["active_laws"].append(choice)
        print(f"{choice} has been passed!")
    elif choice in laws_to_revoke:
        save_data["active_laws"].remove(choice)
        print(f"{choice} has been revoked!")

    print("FORMATION PHASE")
    if save_data["last_formation"]:
        print(f"Previous formation: {save_data['last_formation']}")
        reuse = input("Reuse previous formation? (y/n): ").lower()
        if reuse == "y":
            player_formation = save_data["last_formation"]
        else:
            player_formation = input(f"Choose formation ({'/'.join(FORMATIONS)}): ").upper()
    else:
        player_formation = input(f"Choose formation ({'/'.join(FORMATIONS)}): ").upper()
    save_data["last_formation"] = player_formation

    print("BATTLE PHASE")
    blackspire_formation = random.choice(FORMATIONS)
    result = determine_battle(player_formation, blackspire_formation)
    print(f"Your formation: {player_formation}")
    print(f"Blackspire chose: {blackspire_formation}")
    if result == "victory":
        save_data["player_territory"] += 1
        save_data["blackspire_territory"] -= 1
        print("Result: Victory! Territory gained.")
    elif result == "defeat":
        save_data["player_territory"] -= 1
        save_data["blackspire_territory"] += 1
        print("Result: Defeat! Territory lost.")
    else:
        print("Result: Draw. No territory change.")

    save_data["map"] = generate_map(save_data["player_territory"], save_data["blackspire_territory"], player_symbol=player_symbol)

    print("Options; map / save / exit / continue")
    command = input("Enter command: ").lower()
    if command == "map":
        display_map(save_data["map"])
    elif command == "save":
        with open(SAVE_FILE, "w") as f:
            json.dump(save_data, f, indent=4)
        print("Game saved!")
    elif command == "exit":
        print("Farewell, King!")
        break

    current_turn += 1
