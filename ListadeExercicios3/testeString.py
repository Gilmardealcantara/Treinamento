#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

texto = raw_input('Coloque um texto: ')

i=0;
tam=len(texto)
while i < tam:
	if texto[i] == 'a' or  texto[i] == 'e' or  texto[i] == 'i' or  texto[i] == 'o' or  texto[i] == 'u' :
		texto= texto[:i]+"*"+texto[i+1:]	
	i+=1

print texto

