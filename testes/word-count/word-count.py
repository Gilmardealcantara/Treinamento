#!/usr/bin/python
#-*- coding: iso-8859-15 -*-

'''
	cria um dicionario que mapeia cada palavra e a quantidade de vezes que ela apacere no texto 
'''

arq = open('alice_no_paiz_das_maravilhas.txt')
texto = arq.read()	
texto = texto.lower()

import string
for c in string.punctuation : 
	texto = texto.replace(c, ' ')

texto = texto.split()

dic = {}

for p in texto:
		if p not in dic:
			dic[p] = 1
		else:
			dic[p]+=1

print ('Alice aparece %s vezes' %dic['alice'])

arq.close()

