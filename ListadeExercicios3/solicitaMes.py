#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

meses_ano = ['Janeiro','Fevereiro','Março','Abril','Maio', 'Junho','Julho','Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

data = raw_input('Coloque a data numerica no formato dia/mes/ano: ') 

data=data.split('/')

print (data[0]+" "+meses_ano[int(data[1])-1]+" "+data[2]) 
