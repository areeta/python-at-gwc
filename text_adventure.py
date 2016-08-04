start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room. 
You’re in the front of a cave. A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
You must decide where to go: go inside or leave.
'''
print(start)

decision1 = '''
You decide to go inside. As you walk into the dark cave, fire on the candles placed in cups on the wall instantly lit up.
A very pungent smell looms over the air. Once you are inside, you are given the decision whether to go left or right.
'''
decision2 = ''' "This bush is one of those very dead and brown looking ones. 
Not only do you see rot, there are some shady-looking mushrooms. They seem poisioness, you think.
You debate whether you should walk through the bush or not. Type "yes" to go inside or "no" to leave. '''

bushes1 = ''' You walk through the bush and find yourself in a really big bush. 
For a couple minutes, you are walking through the bush. 
Then, you see a bright light and you ended up at your house safe and sound. 
However, there are a couple spiders on your back from the bushes. '''

bushes2 = ''' "You don't go through the bush and go the other way. 
However, somehow you lose your way and get lost forever. 
From then on, you hate yourself for not going into that ugly-looking bush. '''

choice1 = ''' You are scared but thankful because you haven't seen anyone for awhile but you have human contact. 
This shady looking man comes up to you. As he walks, his cape flashes his skinny, bony legs. 
Then, you realise that this man has a dagger attached to his ankle. You start to run the other way but he runs after you. 
Type "run" to run or "stop" to give up and meet your fate. '''

run = '''You decide to go run. Why would you run? Anyone who has watched a horror movie knows not to run. 
Did you really think you would outrun some shady guy in this story? You die obiviosly. You just lost the game.'''

stop = '''You choose to go stop. The man slams right into you as you stop abruptly. 
As he impacts, you both fall to the ground in the least romantic way. As you stand up, he opens his mouth and says 'Hello. 
I'm super sorry for running after you but it has just been so long since I've had human contact. Also, you kind of ran away from me so I had to go after you.
My name is Jay and I've been lost in this cave for a really long time but good thing, I've been able to stay alive for so long. 
I think we can help each other. From that day on, both of you guys help survive together and eventually get out of the cave.'''

done = True
end = False
start = False
while done: 	
	print("Type 'go inside' to go inside or 'leave' to leave.")
	user_input = input()
	if user_input == "go inside":
		print(decision1) 
		done = False
		while not end: 
			print("Type 'left' to go left or 'right' to go right")
			user_input = input()
			if user_input == "left":
				print("You decide to go left and you see a bush.") 
				end = True
				while not start:
					print(decision2)
					user_input = input()
					if user_input == "yes":
						print(bushes1) 
						start = True
					elif user_input == "no":
						print(bushes2) 
						start = True				
			elif user_input == "right":
				print("You choose to go right and there is a shady-looking man.") 
				end = True
				while not start: 
					print(choice1)
					user_input = input()
					if user_input == "run":
						print(run) 
						start= True
					elif user_input == "stop":
						print(stop)
						start=True				
	elif user_input == "leave":
	    print("You choose to leave and the game is over. You just won the game!!!")
	    done = False



