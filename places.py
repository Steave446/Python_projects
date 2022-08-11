favorite_places = {
	'isaac': ['soudan','duluth','crane lake'],
	'heather': ['seattle','portland','las vegas'],
	'noelle': ['home','paris','switzerland'],
}

print("Favorite Places:\n")

for key, value in favorite_places.items():
	print(f"Name: {key.title()}")
	print(f"Favorite places:")
	for items in value:
		print(f"\t{items.title()}")
	print("\n")