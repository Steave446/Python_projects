favorites = {
	'John' : [4,6,7],
	'kyle' : [2,5,4],
	'jacob' : [17,2,777],
	'edward' : [25, 69]
}
print("favorite numbers:")
for key, value in favorites.items():
	print(key.title())
	for number in value:
		print(f"\t{number}")
