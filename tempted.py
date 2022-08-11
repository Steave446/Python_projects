from time import sleep

t = input("T\n")
if t == 'e':
	sleep(0.5)
	m = input("M\n")
	if m == 'pt':
		sleep(0.5)
		e = input("e\n")
		if e == 'd':
			tempted = "teeeEEEEMptEEEED"
			for letter in tempted:
				print(letter, end ='')
				sleep(0.025)