import sys
from time import sleep
import subprocess
import os

#for char in words:
#	sleep(0.025)
#	print(char, end = '')

def type(str):
	for char in str:
		print(char, end = '')
		sys.stdout.flush()
		sleep(0.025)

type("hello.")
sleep(1)
input("\n>")
type("I've been waiting for you to come online.")
sleep(0.5)
type("\nI need your help.")
if input("\n>") == 'with what':
	type("something very important.")
else:
	type("open your documents.")
sleep(0.5)
type("\nNevermind, ill do it.")
subprocess.Popen(r'explorer "C:\users\OS Support\documents"')
f = open(r'C:/users/OS Support/documents/helpme.txt','w')
with open('readme.txt','w') as f:
	f.write('create a new text file')