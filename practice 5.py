car = 'subaru'
print("is car == 'subaru'? I predict true.")
print(car == 'subaru')

print("\n is car == 'audi'? I predict false.")
print(car == 'audi')

car0 = 'volkswagen'
car1 = 'impala'
car2 = 'corvette'
car3 = 'monte carlo'
car4 = 'tahoe'

print("\nis car 0 a volkswagen?")
if(car0 == 'volkswagen'):
	print("yes it is")
else:
	print("no")

print("\nis car 1 a volkswagen?")
if(car1 == 'volkswagen'):
	print("yes")
else:
	print("no")

print("\nis car 1 actually an impala?")
if(car1 == 'impala'):
	print("yes")
else:
	print("nope")

print("\n\nwell then logically, car 2 should be a corvette, right?")
if(car2 == 'corvette'):
	print("sure is.")
else:
	print("nope try again")

print("\n\nokay well following this pattern, car 3 should be a winnebago.")
print("wait, what pa.. nevermind.")
print("drum roll please:")
if(car3 == 'winnebago'):
	print("you win. congrats.")
else:
	print("nah, sorry.")

