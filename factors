#!/usr/bin/python3
import sys
from check import cleanning, result, compute_non_prime_numbers

""" Function for deleviering result meant for the factor"""


def factor():
	d = sys.argv

	if 1 < len(sys.argv) < 3:
		f = open(d[-1], 'r')
		e = f.readline()
		q = cleanning('\n', list(e))
		while len(e) > 1:
			w, u = compute_non_prime_numbers(q)
			result(w, u, q)
			e = f.readline()
			if len(e) > 0:
				q = cleanning('\n', list(e))
		f.close()


if __name__ == '__main__':
	factor()
