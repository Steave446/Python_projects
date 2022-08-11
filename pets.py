
bob = {
	'name': 'bob',
	'animal': 'dog',
	'age': 3,
	'owner': 'derek',
	'breed': 'golden retriever',
} 

mccree = {
	'name': 'mccree',
	'animal': 'bird',
	'age': 1,
	'owner': 'becca',
	'breed': 'cockatoo',
}

gerald = {
	'name': 'gerald',
	'animal': 'cat',
	'age': 8,
	'owner': 'josh',
	'breed': 'black',
}

pets = [bob, mccree, gerald]

for dict in pets:
	print(f"Pet: {dict['name'].title()}")
	for key, values in dict.items():
		if key != 'name':
			print(f"\t{key}: {values}")
	print('\n')




#	if item['name'] == 'mccree':
#		print("pet name: ", end = '')
#		print(item['name'][0:2].title(), end = '')
#		print(item['name'][2:].title())
#	else:
#		print("pet name: ", end = '')
#		print(item['name'].title())
#	print(f"\tAnimal: {item['animal'].title()}")
#	print(f"\tAge: {item['age']}")
#	print(f"\tOwner: {item['owner'].title()}")
#	print(f"\tBreed: {item['breed'].title()}\n")