#!/usr/bin/python3
# -*- coding: utf-8 -*-

def digits_sum(n):
	return sum([int(i) for i in str(n)])

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def check_complex(k):
	if isint(3*k/digits_sum(k)**2):
		return k, isint(3*k/digits_sum(k)**2), 3*k/digits_sum(k)**2

if __name__ == '__main__':
	print(digits_sum(11))
	for i in range(1,10**2):
		if check_complex(i):
			print(check_complex(i))