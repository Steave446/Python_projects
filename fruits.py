favorite_fruits = ['apples','grapes','bananas']
favorite_fruits.append('oranges')
favorite_fruits.append('potato')
for fruit in favorite_fruits:
	if fruit == 'oranges':
		print("you like oranges")
	elif fruit == 'apples':
		print("you like apples")
	elif fruit == 'bananas':
		print("you like bananas, thats kinda gay bro.")
	elif fruit == 'grapes':
		print("grapes are bussin ong, good choice homie")
	else:
		print(f"{fruit}? what the hell is a {fruit}?\nNo, You know what? get out.")