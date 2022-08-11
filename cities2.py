cities = []
prompt = "\nName a city you have visited:"
prompt += "\nEnter 'quit' when finished."

while True:
	city = input(prompt)

	if city == 'quit':
		print("allegedly, you've visited: ")
		for item in cities:
			print(item.title())
		break
	else:
		cities.append(city)