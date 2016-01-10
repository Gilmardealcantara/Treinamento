#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

def listaRandNoRepead():
	import random
	lista = []
	i=0;
	while  len(lista)<=  15	 : 
		valor = random.randint(10,100)
		f=0
		for j in lista : 
			if j == valor :
				f=1	
				break	
		if f==0 :
			lista.append(valor)
		i+=1

	print lista

listaRandNoRepead()
