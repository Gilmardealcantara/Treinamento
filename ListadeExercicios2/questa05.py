#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

n1 = input('Coloue o primeiro número: ')
n2 = input('Coloue o segundo número: ')
n3 = input('Coloue o tercero número: ')


if n1 > n2 and n1 > n3 : 
	maior=n1
	if n2<n3 :
		menor=n2
	else :
		menor=n3
elif n2>n3 :
	maior=n2
	if n1<n3 :
		menor=n1
	else :
		menor=n3

else :
	maior=n3	
	if n2<n1 :
		menor=n2
	else :
		menor=n1

print ("maior = %d\tmenor = %d" %(maior, menor))
