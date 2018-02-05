#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from sys import argv

global cells
global pointer
global text
cells = [0] * 5000
pointer = 0
text = ""


def get_loop_positions(code):
	start_pos = []
	pos = {}
	for n, c in enumerate(code):
		if c == "[":
			start_pos.append(n)
		elif c == "]":
			start = start_pos.pop()
			pos[start] = n
	return pos

def evaluate_characters(code):
	global cells
	global pointer
	global text
	loop_pos = get_loop_positions(code)
	n = 0
	while n < len(code):
		c = code[n]
		if c == '>':
			if pointer < 4999:
				pointer += 1
			else:
				pointer = 0
		elif c == '<':
			if pointer > 0:
				pointer -= 1
			else:
				pointer = 4999
		elif c == '+':
			if cells[pointer] < 255:
				cells[pointer] += 1
			else:
				cells[pointer] = 0
		elif c == '-':
			if cells[pointer] > 0:
				cells[pointer] -= 1
			else:
				cells[pointer] = 255
		elif c == '.':
			text += chr(cells[pointer])
		elif c == ',':
			cells[pointer] = ord(input())
		elif c == '[':
			while cells[pointer] > 0:
				evaluate_characters(code[n+1:loop_pos[n]])
			n = loop_pos[n]
		n += 1
	return text


if __name__ == "__main__":
	code = ""
	if len(argv) == 2:
		if argv[1].endswith('.bf') or argv[1].endswith('.b'):
			try:
				bf = open(argv[1])
				code = bf.read()
				bf.close()
			except FileNotFoundError:
				print("File not found.")
		else:
			print("Valid file extensions: .b and .bf")
	else:
		code = input()
	if code:
		evaluate_characters(code)
		print(text)