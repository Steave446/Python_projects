from time import sleep

people = {
	'ahsley': {
		'first_name': 'ashley',
		'last_name': 'gaspar',
		'age': 24,
		'city': 'mitchell',
		'state': 'sd',
		'zip_code': '57301',
	},
	'isaac': {
		'first_name': 'isaac',
		'last_name': 'schulte',
		'age': 24,
		'city': 'mitchell',
		'state': 'sd',
		'zip_code': '57301',
	}
}


for person, info in people.items():
	print(f"\nSubject:")
	full_name = f"{info['first_name']} {info['last_name']}"
	location = f"{info['city'].title()}, {info['state'].upper()} - {info['zip_code']}"

	print(f"\tFull name: {full_name.title()}")
	print(f"\tAge: {info['age']}")
	print(f"\tLocation: {location}")