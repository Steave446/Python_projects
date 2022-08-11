cities = {
	'toronto':{
		'country': 'canada',
		'population': '2.93m',
		'fun fact': 'it is the biggest city in canada',
	},
	'ibiza':{
		'country': 'spain',
		'population': '147,914',
		'fun fact': 'one of the liveliest nightlife locations in europe'
	},
	'minneapolis':{
		'country': 'usa',
		'population': '424,536',
		'fun fact': 'considered one and the same with Saint Paul, the city on the other side of the mississippi river from it'
	},
}

print("Cities: ")
for key, item in cities.items():
	print(key.title())
	for key, item in item.items():
		print(f"\t{key.title()}: {item}")
	print("\n")