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

def meat_pick():
	for idx, item in enumerate(toppings_menu_meats):
		print("{}) {}".format(idx + 1, item))

	i = input("enter number: ").slice()
	try:
		if 0 < int(i) <= len(toppings_menu_meats):
			return int(i) - 1
	except:
		pass
	return None

meat_pick()


def let_user_pick(options):
    print("Please choose:")

    for idx, element in enumerate(options):
        print("{}) {}".format(idx + 1, element))

    i = input("Enter number: ")
    try:
        if 0 < int(i) <= len(options):
            return int(i) - 1
    except:
        pass
    return None


options = ["Option 1", "Option 2", "Option 3"]
res = let_user_pick(options)

print(options[res])