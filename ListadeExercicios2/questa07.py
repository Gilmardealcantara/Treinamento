#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import math

tam = input ('Coloque a aréa em metros quadrados: ')

latas = math.ceil(float(float((tam/3))/18))

print ("Voce ira gastar "+ str(latas)+" latas de tinta" )


