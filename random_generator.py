# Write some code to randomly create menu items for a restaurant. Your code should use three lists, each containing different kind of words. 
#Your generator should put 1 word from each list together to create menu items. 
#For example, you could have a list of foods, cooking styles, and an adjective, to create this food:
#“Creamy steamed spinach”  or “Spicy Szechuan chicken”.
#Each list should contain at least 10 items. When the user starts your program your program should list 10 menu items with numbers beside them:
	#1. Creamy steamed spinach
	#2. Spicy Szechuan chicken
import random

cooking_list = ["Fried", "Steamed", "Grilled", "Baked", "Roasted", "Barbecued", "Boiled", "Glazed", "Juiced", "Microwaved" ]
cooking_length = len(cooking_list)
adjective_list = ["Buttery", "Chewy", "Caramelized", "Crispy", "Creamy", "Dry", "Fluffy", "Greasy", "Heavy", "Local" ]
adjective_length = len(adjective_list)
style = ["Chinese", "Korean", "Italian", "American", "Japanese", "Malaysian", "French", "Brazilian", "Indian", "African" ]
style_length = len(style)
food = ["Chicken", "Salmon", "Salad", "Burger", "Steak", "Pasta", "Stew", "Pizza", "Wings", "Curry" ]
food_length = len(food)

print("Please hold as I randomly choose a food for you to eat!")

random_number1 = random.randint(0, cooking_length -1)
random_number2 = random.randint(0, adjective_length -1)
random_number3 = random.randint(0, style_length -1)
random_number4 = random.randint(0, food_length -1)

print(cooking_list[random_number1] + " " + adjective_list[random_number2] + " " + style[random_number3] + " " + food[random_number4])

#Band Name

#Write some code to randomly create band names. 
#Your code should use at least three lists, each containing different kind of words. 
#Your generator should put 1 word from each list together to create menu items. 
#For example, you could have a list of articles, a list of adjectives, and a list of nouns to create “The Rolling Stones,” 

adjectives = ["Adorable", "Beautiful", "Clean", "Drag" "Elegant", "Fancy", "Glamorous", "Handsome", "Long", "Magnificent", "Old-fashioned", "Plain", "Sparkling" ]
adjectives_length = len(adjectives)
color = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Gray", "Black", "White"]
color_length = len(color)
things = ["Spoons", "Bottle caps", "Nail clippers", "Candles", "Ice cubes", "Slippers", "Threads", "Glow sticks", "Needles", "Stop signs", "Chairs"]
things_length = len(things)

print("Please hold as I randomly choose a band name for you!")

random_number5 = random.randint(0, adjectives_length -1)
random_number6 = random.randint(0, color_length -1)
random_number7 = random.randint(0, things_length -1)


print(adjectives[random_number5] + " " + color[random_number6] + " " + things[random_number7])

#Haiku

#Write some code to randomly create haikus. 
#Your code should use two lists - one for lines with 5 syllables, and one for lines with 7 syllables.
#Your generator should put one line with 5 syllables followed by another line with 7 syllables, followed by another line with 5 again. 
#Print 3 haikus. Each list should contain at least 10 items. 

#When the user starts your program, your program should print out 3 haikus, with a line between them:

five_sy = ["An old silent pond,", "Lightning flash,", "Keep calm and tweet on!", "Eat your vegetables!", "Who is our speaker?", "I want Lucky Charms!", "Iron man is great!", "I want food right now!", "Glow sticks are fancy!", "I like cookies a lot!"]
five = len(five_sy)
seven_sy = ["On Sundays, I like to eat", "Twitter Twenty is so real!", "You suck but you're growing!", "Mel is short for awesome", "Jasmine is interestings!", "Today is flannel friday!", "X location minus y!", "Rhae likes to wrestle and run!", "Phoenix is obsessed with Jack"]
seven = len(seven_sy)



for i in range(3):
	random_number8 = random.randint(0, five - 1)
	random_number9 = random.randint(0, seven -1)
	print(five_sy[random_number8])
	print(seven_sy[random_number9])
	random_number8 = random.randint(0, five - 1)
	print(five_sy[random_number8])
	
	print()







