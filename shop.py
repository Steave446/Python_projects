stock = {
	'lamp oil': 5,
	'rope': 10,
	'bombs': 20,
}

print(*stock, "you want it? it's yours my friend. as long as you have enough rupees.\n ",sep = ', ')

rupees = 15

for key, value in stock.items():
	print(key," -- ",value)
print(f"\nRupees: {rupees}")

def price_check():
	global stock
	global rupees
	cart = input("what would you like? ")
	if cart in stock.keys():
		x = stock.get(f"{cart}")
		if rupees >= x:
			print("here you go")
			print(f"+1 {cart}")
		elif rupees < x:
			print("Sorry Link, I can't give credit. Come back when you're a little, mmm... Richer.")
	else:
		print('selection invalid')

price_check()