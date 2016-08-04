from hashlib import * # * means to import all

def hash(password):
	return sha256(password.encode('utf-8')).hexdigest()

username = input("What's your username? ")

inventory = {}

done = True
if username in inventory:
	password = input("What's your password? ")
	if inventory[username] == hash(password):
		print("You're in!")
elif not username in inventory:
	print("Incorrect username. You are not signed up yet. ")
	password = input("Please enter a password.")
	hash(password)
	inventory[username] = hash(password)
	print("You are able to login now with the following username: " + username)
	print(inventory)

	while done:
		username = input("What's your username? ")
		if username in inventory:
			password = input("What's your password? ")

		if inventory[username] == hash(password):
			print("You're in!")
			done = False
		elif inventory[username] != hash(password):
			print("You're not in!")
			done = True