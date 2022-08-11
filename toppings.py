from time import sleep
#code based on user input for a two topping pizza
default_toppings = ['tomato sauce', 'cheese','hand-tossed crust']
crust_types = ['hand-tossed','handmade pan','thin']
requested_topping = []
sizes = ['extra-large','large','medium','small','personal']
extra_toppings = ['mushrooms','bell peppers','black olives','onions']
meats = ['bacon','sausage','pepperoni','canadian bacon']
current_order = {
	'crust': '',
	'toppings': ['']
}

######################################################################

print("Hello, welcome to dominos, what can we get for you?")
sleep(1)

#request = input()
#if request != 'pizza':
#	print("get out now")
#	quit()
print("sounds good,")
print("lets get you started.")
print("\n\nLet's start with the crust, which would you like?")

######################################################################
for crusts in crust_types:
	print(f"\t{crusts.title()}")
	sleep(0.25)

crust_choice = input("Crust:")

for crust_pick in crust_choice:
	if crust_choice not in crust_types:
		sleep(0.5)
		print('sorry thats not one of the choices.')
		sleep(0.75)
		print('which one would you like?')
		sleep(0.5)
		for crusts in crust_types:
			print(f"\t{crusts}")
			sleep(0.25)
		crust_choice = input("Crust:")
	else:

		print(f"youve selected {crust_choice.title()} crust. Is that correct?")
		if input("y/n:") == 'y':
			print("thanks.")
			current_order[2] = crust_choice  
			break
		else:
			print("sorry")
			sleep(0.5)
			print("which crust would you like?")
			for crusts in crust_types:
				print(crusts)
			crust_choice = input()
sleep(0.5)

######################################################################

print("\nHow about the size?")
for size in sizes:
	print(size.title())

size_choice = input()
for confirmation in size_choice:
	if size_choice not in sizes:
		print("Sorry, thats not one of the choices")
		print("which size would you like?")
		sleep(0.5)
		for size in sizes:
			print(size.title())
			sleep(0.5)
		size_choice = input()
	else:


		print(f"youve selected {size_choice}, is that correct? y/n")
		if input() == 'y':
			print("thank you")
			current_order['crust']
			break
		else:
			print("sorry, what was that?")

######################################################################

print(f"okay, so far we have a {size_choice}, {crust_choice} crust pizza.")
sleep(0.5)
print("moving on.")
sleep(1)

######################################################################

print("How about the extras?")
print("veggies\t\tmeats")
print("----------------------")
for i in range(len(extra_toppings)):
	print(extra_toppings[i] + "\t" + meats[i])

extras = []
extras = input("extras:").split()

print("\nOkay so you want:")
for ingredient in extras:
	if ingredient in extra_toppings:
		extras.append(ingredient)
		print(ingredient)
	elif ingredients in meats:
		extras.append(ingredient)
		print(ingredient)
	else:
		print(f"sorry, {ingredient} is invalid")
		print("veggies\t\tmeats")
		print("----------------------")
		for i in range(len(extra_toppings)):
			print(extra_toppings[i] + "\t" + meats[i])
		extras=input("extras:").split()
		print(f"selected: {extras}")

print("is that correct?")
extras_confirmation = input("y/n:")
if extras_confirmation == 'y':
	print("accepted")
else:
	print("i guess not")
