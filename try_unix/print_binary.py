#!/usr/bin/python
import sys
arg = sys.argv[1:]
for items in arg:
	if int(items) < 0:
		print 'Value less than zero'
	else:
		binary = '' 
		ONE = 1
		temp = int(items)
		while True:
			binary += str(temp & ONE)
			temp = temp >> 1
			if temp == 0 :
				break
		print 'Binary of ', items , ' is - ', binary[::-1]
			
		
