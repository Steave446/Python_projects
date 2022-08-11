my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("my favorite foods are:")
for food in my_foods:
	print(food)

print("\nmy friends favorite foods are:")
for food in friend_foods:
	print(food)

print("\nthe first three foods in my list are:")
for food in my_foods[0:3]:
	print(food)


print("\nthe middle three items in my list are:")
for food in my_foods[1:4]:
	print(food)


my_foods.append('coffee cake')
print("\nthe last three items:")
for food in my_foods[-3:]:
	print(food)
