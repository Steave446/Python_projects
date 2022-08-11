available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

if requested_toppings:
	for requested_topping in requested_toppings:
		if requested_topping in available_toppings:
			print(f"Adding {requested_topping}.")
		else:
			print(f"sorry, {requested_topping} does not belong on pizza")
	print("\nPizza finished.")
else:
	print("bro what are you, that guy from 4chan? 'none pizza left beef' lookin ass, man add some damn toppings.")