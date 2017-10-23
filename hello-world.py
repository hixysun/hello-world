# hello-world.py

import sys
import argparse

def printHello(args):
	if len(args) == 0:
		print 'hello world.'
	elif len(args) == 1:
		print 'hello world, ', args[1]
	else:
		print 'too many input values.'


if __name__ == '__main__':
	parser = argparse.ArgumentParser('hello')
	args = vars(parser.parse_args())
	print 'type: ', type(args)
	printHello(args)