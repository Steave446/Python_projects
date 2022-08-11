age = int(input("how old are you?\n"))
if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40

print(f"{if age < 4 (print('hello'))} ${price}")