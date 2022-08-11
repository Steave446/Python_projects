for value in range(1,5):
	print(value)
	#in range(1,5), 5 represents the stopping point for the range, and will stop at the number just before.

#in order to print 1-5, the code must be written as such:
for value in range(1,6):
	print(value)

#using range to make a list of numbers
numbers=list(range(1,6))
print(numbers)

even_numbers=list(range(2,11,2))
#list(range(starting at, going to, counting by))
print(even_numbers)

squares = [] #start by making an empty list
for value in range(1,11):
#tell python to loop through each value from 1 to 10 using the range function

	square = value**2 
	# inside the loop, the current value is raised to the seocnd power and assigned to the variable square

	squares.append(square) 
	#each new value is then appended to the squares list
	#This can be written more concisely

print(squares)

squares2 = []
for value in range(1,11):
	squares2.append(value**2)

print(squares2)
#by combining both statements in the loop, you can make that code more concise without sacrificing functionality.

#simple statistics
digits = range(1,11)
print(min(digits))
print(max(digits))
print(sum(digits))


#list comprehensions - allows you to write a loop in a single line of code.
squares3 = [value**2 for value in range(1,11)]
print(squares3)
#ez

#counting to 20
counting = [value for value in range(1,21)]
print(counting)

#counting to 1 million
million = [value for value in range(1,1000001)]
print(min(million))
print(max(million))
print(sum(million))

#counting by odd numbers
odd_numbers = [value for value in range(1,11,2)]
print(odd_numbers)

#counting by threes
threes = [value for value in range(3,31,3)]
print(threes)

#cubes
cubes1 = [value**3 for value in range(1,11)]
print(cubes1)

#cubes = [value**3 for value in range(1,11)]
#for value in cubes:
	#print(value)