#!/usr/bin/python  
# -*- coding: iso-8859-15 -*-


#verificar se um anor é bisexto  
# se for divisivel por 4 e nao acaber em '00' - ok
# se sim (acabar em '00')ver se é divisivel por 400 se sim  - ok 

ano = int(input('Insira o ano: ')) 
  
if ano%4==0 : 

	if str(ano)[ len(str(ano)) -1 ] == "0" and str(ano)[ len(str(ano)) -2 ] == "0" : 
		if ano%400 == 0 : 
			print ("É Bisexto")
		else:
			print ("Não é Bissexto")

	else:
		print ("É Bisexto")

else:
	print 'Não é bissexto.'
