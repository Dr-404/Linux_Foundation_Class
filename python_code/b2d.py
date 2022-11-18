#!/usr/bin/env python3

bi = int(input("Enter Binary Number : "))


dec = 0
i = 0 


def new_binary (x):
	x = x//10
	return x

def reaminder (x):
	x = x%10
	return x


while bi != 0:

	a = reaminder(bi)
	dec = dec  + (a*pow(2,i))
	i = i+1
	bi = new_binary(bi)


print(dec)