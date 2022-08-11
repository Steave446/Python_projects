import csv
import os
import sys

dictfromreader = {
	
}
with open('contactstest.csv') as inp:
	lst = [*csv.DictReader(inp)]
	for item in lst:
		print(item)