#!/usr/bin/python3
import sys
from check import ( cleanning, compute_prime_numbers, result)

""" Function for running the prime number forum"""


def rsa():
	d = sys.argv
	if len(d) == 2:
		f = open(sys.argv[-1], 'r')
		e = f.readline()
		q = cleanning('\n', list(e))
		while len(e) > 0:
			w, u = compute_prime_numbers(q)
			result(w, u, q)
			e = f.readline()
			if len(e) > 0:
				q = cleanning('\n', list(e))
		f.close()


if __name__ == '__main__':
	rsa()
