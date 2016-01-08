#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

def  fat(x):
	f=1
	for i in range(1,x+1) :
		f*=i;
	return f	

n = input('Coloque um numero: ')
print fat(n)
