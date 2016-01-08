#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

var1 = raw_input('Coloque uma palavra: ')

if var1 == var1[::-1] :
	print(var1+" é Palindrome")
else :	
	print(var1+" não é Palindromes")
