#!/usr/bin/env python

import re
strings = open('nice_strings.txt','r')
nice_strings = []

for line in strings:
	line = line.strip()

	forbid = re.search(r"(ab|cd|pq|xy)", line)
	if forbid != None:
		continue
		
	vowels = re.findall(r"[aeiou]", line) 
	if vowels != None:
		if len(vowels) < 3:			
			continue
	
	double = re.search(r"(.)\1", line)
	if double == None:
		continue
	
	nice_strings.append(line)
					
print len(nice_strings)