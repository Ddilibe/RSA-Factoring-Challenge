#!/usr/bin/python3
from prime import Prime
"""
This document is used for cleaning the data set
It also contains other related functions
"""

""" FUnction for cleanning a line of value from a file """


def cleanning(word, listing):
	if word in listing:
		listing.remove(word)
	listing = ''.join(listing)
	listing = int(listing)
	return (listing)


""" Function for displaying the result from an analysis """


def result(i, k, y):
	print("{}={}*{}".format(y, k, i))


""" Function for obtaining a list of over 10,000
prime numbers inputed in a jjson file """


# def obtain_prime_numbers():
# 	with open('prime.json', 'r') as file:
# 		numbers = json.load(file)
# 		prime = numbers['Prime']
# 		file.close()
# 		return (prime)


""" Function for computing  and delivering the prime numbers """


def compute_prime_numbers(value):
	prime = Prime()
	i = 2
	while True:
		w = value % i
		if w == 0:
			if i in prime:
				return (i, int(value / i))
		i += 1


""" Functions for computing and delivering the non prime numbers"""


def compute_non_prime_numbers(value):
	w = 2
	while (value % w != 0):
		w += 1
	return (w, int(value/w))
