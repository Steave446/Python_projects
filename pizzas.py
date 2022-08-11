pizzas = ['pepperoni','sausage','canadian bacon','supreme']

print("here are some types of pizza toppings:\n")
for toppings in pizzas:
    print(f"{toppings} pizza is good.")

print("\ntheyre all decent ngl")


friend_pizza = pizzas[0:]

pizzas.append('anchovy')

friend_pizza.append('cheeseburger')

print("\nmy favorite pizzas are:")
for toppings in pizzas:
    print(toppings.title())

print("\nmy friend however:")
for toppings in friend_pizza:
    print(toppings.title())

print("F#$%#ing copycat")

