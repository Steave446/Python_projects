def city_country(city,country):
	if country == 'usa':
		print(f"{city.title()} is a city in the {country.upper()}")
	else:
		print(f"{city.title()} is a city in {country.title()}")


cities = {
	'santiago': 'chile',
	'minneapolis': 'usa',
	'paris': 'france',
}

for key, value in cities.items():
	city_country(key,value)