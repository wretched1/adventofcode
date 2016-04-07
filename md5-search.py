#!/usr/bin/env python

import hashlib, re

puzzle_input = "ckczppom"
count = 0

while True:
	check = puzzle_input + str(count)
	md5_val = hashlib.md5(check)
	hex_val = md5_val.hexdigest()
	if hex_val[:5] == "00000":
		print hex_val, check
		exit()
	count += 1