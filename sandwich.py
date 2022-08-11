sandwich_orders = ['BLT','ham & cheese','chicken bacon ranch','pastrami','pastrami','pastrami']
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
for sammies in sandwich_orders:
	print(f"i made you a {sammies} sandwich")
	finished_sandwiches.append(sammies)

for sammies in finished_sandwiches:
	print(sammies)