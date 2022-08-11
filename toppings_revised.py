from time import sleep

######## Define current order with default parameters
current_order = {'crust': 'handmade pan',
				'sauce': 'tomato',
				'toppings': {'meats': ['',],
							'veggies': ['cheese',]
							},

	'extra cheese': 0,
	'size': 'medium',
}
############### MENU ##############
crust_menu = [
	'hand tossed',
	'handmade pan',
	'thin'
	]

toppings_menu_meats = [
	'salami',
	'pepperoni',
	'bacon',
	'beef',
	'canadian bacon',
	'italian sausage',
	'philly steak',
	'premium chicken'
	]

toppings_menu_veggies = [
	'mushrooms',
	'pepers',
	'diced tomatoes',
	'onions',
	'spinach',
	'jalapenos',
	'black olives',
	'olives',
	'pineapple',
	'hot buffalo sauce'
	]

size_menu = [
	'personal',
	'small',
	'medium',
	'large',
	'extra large'
	]

################# Code Begin ###########

def cheese_grab():
	if current_order.get('extra cheese') == 0:
		print("No")
	elif current_order.get('extra cheese') == 1:
		print("Yes")

crust_pick = ''
fail_check = {
	'crust': 'yes',
	'size': 'yes',
	'meats': 'yes',
	'veggies': 'yes',
	'extra_cheese': 'yes'
}

def crust_check():
	global fail_check
	if crust_pick in crust_menu:
		print(f"\nyou've selected {crust_pick.title()} crust.")
		print("is that correct?")
		confirm = input("y/n: ")
		if confirm == 'y':
			print('thank you\n')
			fail_check['crust'] = 'no'
		elif confirm == 'n':
			print('\nsorry, lets try that again.')
			fail_check['crust'] = 'yes'
	else:
		print(f"sorry, {crust_pick} is not an option")

def size_check():
	global fail_check
	if size_pick in size_menu:
		print(f"\nyou've selected a {size_pick.title()} pizza.")
		print("is that correct?")
		confirm = input("y/n: ")
		if confirm == 'y':
			print("thanks.\n")
			fail_check['size'] = 'no'
		elif confirm == 'n':
			print('\nsorry, lets try that again.')
			fail_check['size'] = 'yes'
	else:
		print(f"sorry, '{size_pick}' is not an option.")

def meats_check():
	global fail_check
	for item in meats_pick:
		if item not in toppings_menu_meats:
			print(f"{item} is invalid")
			break
	print("youve selected:")
	for item in meats_pick:
		if item in toppings_menu_meats:
			print(item.title())
	print("\nis that correct?")
	confirm = input("y/n:")
	if confirm == 'y':
		print("thanks.")
		fail_check['meats'] = 'no'
	elif confirm == 'n':
		print("sorry, let's try again")
		fail_check['meats'] = 'yes'

def veggies_check():
	global fail_check
	for item in veggies_pick:
		if item not in toppings_menu_veggies:
			print(f"sorry, {item} is invalid.")
			break
	print("you've selected: ")
	for item in veggies_pick:
		if item in toppings_menu_veggies:
			print(item.title())
	print("\nIs that correct?")
	confirm = input("y/n: ")
	if confirm == 'y':
		print("Thanks")
		fail_check['veggies'] = 'no'
	elif confirm == 'n':
		print("Sorry, lets try again.")
		fail_check['veggies'] = 'yes'


print("dominos CLI ordering (BETA)\n")

search = 'cheese'

print("Starting with default order:")
for item in current_order:

	if item == 'extra cheese':
		print(f"{item.title()}?: ", end = ''), cheese_grab()

	elif item == 'toppings':
		print(f"{item.title()}: ")

		for item in current_order.get('toppings'):
			if item == search:
				continue
			elif item != search:
				print(f"\t{item.title()}")

	else:
		print(f"{item.title()}: {current_order.get(item)}")

print("\nCrust selection:\n")
while fail_check['crust'] == 'yes':
	print("Here are your options:\n")
	for crust in crust_menu:
		print(f"{crust.title()}")
	crust_pick = input("\ncrust: ")
	crust_check()
print(f"crust fail check: ", end = ''),(print(fail_check.get('crust')))

print(f"\nSize:\n")
while fail_check['size'] == 'yes':
	print("Here are our sizes: ")
	for size in size_menu:
		print(size.title())
	size_pick = input("\nsize: ")
	size_check()
print("\nMoving on.\n")

print("Let's pick our meats, yeah?")
while fail_check['meats'] == 'yes':
	print("meats:\n")
	for item in toppings_menu_meats:
		print(item.title())
	meats_pick = input("\nMeats:").split()
	meats_check()

print("moving on to veggies:")
while fail_check['veggies'] == 'yes':
	for item in toppings_menu_veggies:
		print(item.title())
	veggies_pick = input("Choose now: ").split()
	veggies_check()

print(crust_pick)
print(size_pick)
print(meats_pick)
print(veggies_pick)
