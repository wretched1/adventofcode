#!/usr/bin/env python

import re
strings = open('nice_strings.txt','r')
nice_strings = []

for line in strings:
	line = line.strip()

	repeat = re.search(r"([a-z]{2,3}).*\1", line)
	if repeat == None:
		continue
		
	double = re.search(r"([a-z])((?!\1).)\1", line)
	if double == None:
		continue
	
	nice_strings.append(line)
					
print len(nice_strings)