import time

name = input("Greeting my fair king! what shall I call you!: ").capitalize()
print (f"Well hello King {name}, I am the Court Jester!")
time.sleep(1)
kingdom = input(f"Now King {name}, excuse my absentmindedness but what was the name of our kingdom again?:").capitalize()
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
#shoutout jay thy gay