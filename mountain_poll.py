responses = {}

polling_active = True

while polling_active:
	name = input("\nwhat is your name?")
	response = input("which mountain would you like to climb someday?")

	responses[name] = response

	repeat = input("Another poll? (Y/N)")
	if repeat == 'no':
		polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(f"{name} would like to climb {response}")
	