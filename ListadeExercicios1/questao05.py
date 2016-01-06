val_merc = float (input('Coloque o Valor da Mercadoria : '))
per = str(input('Coloque a percentual de desconto : '))

per=float("0."+per)
print per

print ("Desconto :"+str(val_merc*per)+" reais\nNovo val_mercario : "+str(val_merc-(val_merc*per))+" reais")
