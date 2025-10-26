import time
import json
import os

SAVE_FILE = "save.json"

if not os.path.exists(SAVE_FILE):
	print ("creating save")
	save_data = {
	"name": None,
	"kingdom": None,
	"gold": 0,
	"progress": {},
	"character_created": False
	}
	with open (SAVE_FILE, "w") as f:
		json.dump(save_data, f, indent=4)
else:
		print("loading save")
		with open(SAVE_FILE, "r") as f:
			save_data = json.load(f)

			if save_data["character_created"]:
				print(f"Welcome back, King {save_data['name']} of {save_data['kingdom']}!")

			else:
				name = input("Greeting my fair king! what shall I call you!: ").capitalize()
				save_data["name"] = name
				print (f"Well hello King {name}, I am the Court Jester!")
				time.sleep(1)
				kingdom = input(f"Now King {name}, excuse my absentmindedness but what was the name of our kingdom again?:").capitalize()
				save_data["kingdom"] = kingdom
				print (f"Oh yes! how could I forget the glorious kingdom of {kingdom}!")
				time.sleep(1)
				first_invalid = True
				while True:
					irrelevent_q1 = input("Are you familiar with the state of the nation? Y or N")
					if irrelevent_q1 in ["y", "Y"]:
						print (f"Perfect! then no time will be wasted King {name}!")
						break
					elif irrelevent_q1 in ["n", "N"]:
						print ("Now from what I have heard,")
						time.sleep(2)
						print ("please do excuse me if I am wrong, no one really takes a silly old Court Jester too seriously.")
						time.sleep(3)
						print ("Your brother was a tad bit egotistical, and he left our fine kingdom in extreme disarray.")
						time.sleep(3)
						print ("He started his term by starting war with the biggest baddest kingdom on the block, Blackspire.")
						time.sleep(3)
						print ("And then the cherry on top! he introduced crazy taxes, 48.65%!")
						time.sleep(3)
						print ("If you didn't want to pay those taxes, you had to join the military. Which was certain death, Blackspire was ruthless!")
						time.sleep(6)
						break
					else:
						if first_invalid:
							print ("Y or N")
							first_invalid = False
							print("Now you should be well acquainted with the state of our nations, I feel that you will be able to get our kingdom to be the most prosperous of all time!")
							save_data["character_created"] = True
							with open(SAVE_FILE, "w") as f:
								json.dump(save_data, f, indent=4)
