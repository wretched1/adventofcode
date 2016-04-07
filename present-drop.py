#!/usr/bin/env python
# For advent challenge, day 

santa_loc = (0, 0)
robo_loc = (0, 0)
house_locations = set()
house_locations.add(santa_loc)
house_locations.add(robo_loc)
is_robo = False

directions = open('houses.txt','r')

def santa(char,santa_loc):
	if char == "^":
		santa_loc = (santa_loc[0],santa_loc[1]+1)
	elif char == "v":
		santa_loc = (santa_loc[0],santa_loc[1]-1)
	elif char == "<":
		santa_loc = (santa_loc[0]-1,santa_loc[1])
	elif char == ">":
		santa_loc = (santa_loc[0]+1,santa_loc[1])
	else:
		print "Couldn't identify the character."
	return santa_loc

def robo(char,robo_loc):
	if char == "^":
		robo_loc = (robo_loc[0],robo_loc[1]+1)
	elif char == "v":
		robo_loc = (robo_loc[0],robo_loc[1]-1)
	elif char == "<":
		robo_loc = (robo_loc[0]-1,robo_loc[1])
	elif char == ">":
		robo_loc = (robo_loc[0]+1,robo_loc[1])
	else:
		print "Couldn't identify the character."
	return robo_loc		

	
for line in directions:
	for char in line.rstrip():
		if is_robo == False:
			#print 'Santa'
			santa_loc = santa(char,santa_loc)
			house_locations.add(santa_loc)
			is_robo = True
		elif is_robo == True:
			#print 'Robo'
			robo_loc = robo(char,robo_loc)
			house_locations.add(robo_loc)
			is_robo = False
		
print len(house_locations)