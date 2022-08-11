items = ['one','two','three','four','five']

for item in items:
	if item in items[0:-1]:
		print(f"{item}, ", end = '')
	else:
		print(f"and {item}.")