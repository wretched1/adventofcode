#! /usr/bin/env python

data = open('boxes.txt')

total = 0

def smallest_side(l,w,h):
	if h <= w:
		if w <= l:
			#print "option 1"
			extra = h * w
			return extra
	if w <= h:
		if l <= h:
			#print "option 2"
			extra = w * l
			return extra
	if l <= h:
		if h <= w:
			#print "option 3"
			extra = l * h
			return extra
	

for line in data:
	extra = 0
	line = line.rstrip()
	box_dim = line.split('x')
	box_dim = list(map(int,box_dim))
	box_dim.sort()
	l = box_dim[0]
	w = box_dim[1]
	h = box_dim[2]
	
	extra = smallest_side(l,w,h)
	total = total + l*w*2 + l*h*2 + w*h*2 + extra

data.close()
print total
