#!/usr/bin/python
#-*- coding: iso-8859-15 -*-

peso = int(input('Coloque o Peso : '))

excesso = peso-50
multa = excesso*4

if peso < 50 : 
	excesso=0
	multa=0
	
print("execesso = %d\nmulta= %d" %(excesso, multa))

