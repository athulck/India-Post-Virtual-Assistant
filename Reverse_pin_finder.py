import os
import csv
import subprocess as sp

def find_pin(pin):

	found = False
	string = ""

	with open('data.txt', newline='\n') as file:
		reader = csv.reader(file, delimiter=',', quoting=csv.QUOTE_NONE)
		
		for row in reader:
			if (pin == row[8]):
				string += ', '.join(row[:9]) + '\n'
				found = True

		if (found):
			f = open('PinSearchResult.txt', 'w', encoding='utf-8')
			f.write(string)
			sp.call(['gedit', 'PinSearchResult.txt'])

		return found
