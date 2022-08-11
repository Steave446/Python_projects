number = input("enter a number: ")
number = int(number)
is_number_mult = False
if number % 10 == 0:
	is_number_mult = True
	print("multiple of 10")
else:
	print('not multiple of 10')

print(is_number_mult)