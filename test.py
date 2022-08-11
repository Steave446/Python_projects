print("How about the extras?")
print("veggies\t\tmeats")
print("----------------------")
for i in range(len(extra_toppings)):
	print(extra_toppings[i] + "\t" + meats[i])

extras = []
extras = input("extras:").split()

print("\nOkay so you want:")
for ingredients in extras:
	if ingredients in extra_toppings:
		extras.append(ingredients)
		print(ingredients)
		break
	elif ingredients in meats:
		extras.append(ingredients)
		print(ingredients)
		break
	else:
		print(f"sorry, {ingredients} is invalid")
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