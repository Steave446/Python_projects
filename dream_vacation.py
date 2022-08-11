dream_vacations = {
	
}
print("what is your dream vacation spot?")

active = True

while active:
	name = input("name please: ")
	location = input("dream destination: ")
	dream_vacations[name] = location
	print("thank you.")
	confirmed = False
	while confirmed == False:
		proceed = input("continue? Y/N: ") 
		if  proceed == 'n':
			confirmed = True
			active = False
			break
		elif proceed == 'y':
			confirmed = True
			continue
		else:
			print("invalid")



print("--- Poll Results ---")
for key, value in dream_vacations.items():
	print(f"{key.title()} would like to visit {value} someday.")