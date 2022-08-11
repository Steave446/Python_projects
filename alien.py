alien_0 = {
		'color': 'green', 
		'points': 5, 
		'x_pos': 0, 
		'y_pos': 25
		}

print(f"Original position: {alien_0['x_pos']}")
alien_0['speed'] = 'medium'
#move alien to the right
#determine how far the alien moves based on its current speed

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#assumed fast alien
	x_increment = 3

alien_0['x_pos'] = alien_0['x_pos'] + x_increment

print(f"new position: {alien_0['x_pos']}")