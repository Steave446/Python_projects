from time import sleep
words = "this is a test"
for char in words:
	sleep(0.025)
	print(char, end='', flush=True)
	