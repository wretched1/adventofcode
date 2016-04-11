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

def switch(action, start, stop):
	start = split_pos(start)
	stop = split_pos(stop)
	for i in range(start[0], stop[0]):
		for x in range(start[1], stop[1]):
			position = "%s,%s" %(str(i),str(x))
			if action == 'toggle':
				if grid[position] == 0:
					grid[position] = 1
				else:
					grid[position] = 0
			elif action == 'on':
				grid[position] = 1
			else:
				grid[position] = 0

	
for line in puzzle:
	line_parts = line.split(' ')
	start = line_parts[-3]
	stop = line_parts[-1]
	if re.match(r'^toggle', line_parts[0]):
		switch('toggle', start, stop)
	elif re.match(r'^turn on', line):
		switch('on', start, stop)
	else:
		switch('off', start, stop)
		
puzzle.close()
light_count = 0
for key in grid:
	if grid[key] == 1:
		light_count += 1
		
print "Total lights: %s" %(str(light_count))