current_usernames = ['moomoo','Intervention','kawaii_panda','admin','george']
new_usernames = ['becca','arnold','intervention','gert','toby']
current_usernames_lower = []

for user in current_usernames:
	user = user.lower()
	current_usernames_lower.append(user)
print(f"current users as input{current_usernames}")
print(f"current users in lowercase: {current_usernames_lower}")

for user in new_usernames:
	if user in current_usernames:
		print(f"sorry, username '{user}' is taken.")
	elif user in current_usernames_lower:
		print(f"sorry, username {user} is taken")
	else:
		print(f"Hi, {user}! Thank you for registering!")
		current_usernames.append(user)

print("current users:")
for user in current_usernames:
	print(user)