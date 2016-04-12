#!/usr/bin/env python

import re

puzzle = open('puzzle-input.txt', 'r')

# Create the grid
grid = {}
for i in range(0,1000):
	for x in range(0,1000):
		position = "%s,%s" %(str(i), str(x))
		grid[position] = 0

def split_pos(pos):
	pos = pos.split(',')
	pos = map(int,pos)
	return pos

def brightness(action, start, stop):
	start = split_pos(start)
	stop = split_pos(stop)
	for i in range(start[0], stop[0]+1):
		for x in range(start[1], stop[1]+1):
			position = "%s,%s" %(str(i),str(x))
			#print "Working on Position: %s" %position #Used for troubleshooting
			if action == 'toggle':
				current = grid[position]
				new = current + 2
				grid[position] = new
			elif action == 'on':
				current = grid[position]
				new = current + 1
				grid[position] = new
			else:
				current = grid[position]
				if current != 0:
					new = current - 1
					grid[position] = new

	
for line in puzzle:
	line_parts = line.split(' ')
	start = line_parts[-3]
	stop = line_parts[-1].strip()
	if re.match(r'^toggle', line_parts[0]):
		brightness('toggle', start, stop)
	elif re.match(r'^turn on', line):
		brightness('on', start, stop)
	else:
		brightness('off', start, stop)
		
puzzle.close()
# Count 'em up
total_brightness = 0
for key in grid:
	if grid[key] != 0:
		total_brightness += grid[key]
		
print "Total Brightness: %s" %(str(total_brightness))