#!/usr/bin/python
#-*- coding: iso-8859-15 -*-

#Pega o preço do café na pagina abaixo 
import urllib
import time

def pega_preco():
	pagina = urllib.urlopen('http://beans.itcarlow.ie/prices.html')
	texto = pagina.read().decode('utf8')
	onde = texto.find('>$')
	preco = float(texto[onde+2:onde+4])
	return preco


opcao = raw_input('Deseja Compra agorar? (S/N) ')

if opcao == 'S':
	preco = pega_preco()
	print ('Comprar! Preço: %5.2f' %preco)
else:
	preco = 99.99
	while preco >= 5.00:  
		preco = pega_preco()
		if preco >= 5.00: 
			print ('Não comprar!!! Preço: %5.2f' %preco)
			time.sleep(10)
	print ('Comprar! Preço: %5.2f' %preco)



