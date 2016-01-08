#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
#assumindo q zero é triagular superior 

n = int(input('Coloque um número: '))

i=0
j=1
k=2
produto = n-1;
while produto <= n :
	produto = i*j*k
	if produto == n :
		print ("O numéro "+str(n)+" é triangular pois é igual a "+str(i)+"*"+str(j)+"*"+str(k))
		exit()
	i+=1
	j+=1
	k+=1
print ("O numero "+str(n)+" não é triangular")
