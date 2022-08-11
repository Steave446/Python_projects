players = ['charles','martina','michael','florence','eli']
print(players[0:3])
#print(players[starting at:going to]) (AKA stopping at the third value in the list, technically the fourth)

print(players[1:4])
#dont have to start at 0

#omitting the starting point starts the slice at the beginning of the list
print(players[:4])

#can also omit the end point, printing the whole list starting at the specified point
print(players[0:])

#can also use negative values to determine a starting point a certain length from the end
print(players[-3:])

#Looping through a slice
print("here are the first three players on the team:")
for player in players[:3]:
	print(player.title())