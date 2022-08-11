user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}

for key, value in user_0.items():
	if key == 'username':
		print(f"Username: {value}")
	elif key == 'first' or 'last':
		print(f"{user_0['last']}, {user_0['first']}")
	else:
		print("done")