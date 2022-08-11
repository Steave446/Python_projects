banned = ['charlie','fred','amy']
shadowbanned = ['dalton','corey','fran']

history = []
lookup = input("search banned users here:").split()

for user in lookup:
	if user in banned:
		print(f"{user} is banned.")
		history.append(user)
	elif user in shadowbanned:
		print(f"{user} is shadowbanned.")
		history.append(user)
	else:
		print(f"{user} not found in ban list.")

print("you have searched:")
for user in history:
	print(user)
print("is this correct?")
correct = input("y/n:")
if correct == y:
	print("thank you for searching")
else:
	print("sorry, try again later")
	return(5)
