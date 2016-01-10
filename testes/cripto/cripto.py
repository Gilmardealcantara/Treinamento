#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

arq = open('msg_cripto.txt', 'w')
with open('ola_eu_sou_o_goku.txt') as f:
	s = f.read()
	aux=""
	for i in list(s):
		if i in 'aeiouAEIOU' :
			aux+='*'
		else :
			aux+=i
	arq.write(aux)
arq.close()
