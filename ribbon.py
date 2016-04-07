#! /usr/bin/env python

data = open('boxes.txt')

total = 0

def smallest_side(l,w,h):
	if h <= w:
		if w <= l:
			ribbon = h + h + w + w
			return ribbon
	if w <= h:
		if l <= h:
			ribbon = w + w + l + l
			return ribbon
	if l <= h:
		if h <= w:
			ribbon = l + l + h + h
			return ribbon
	

for line in data:
	line = line.rstrip()
	box_dim = line.split('x')
	box_dim = list(map(int,box_dim))
	box_dim.sort()
	l = box_dim[0]
	w = box_dim[1]
	h = box_dim[2]
	bow = l * w * h
	ribbon = smallest_side(l,w,h)
	
	total = total + bow + ribbon

data.close()
print total