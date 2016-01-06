sal = float (input('Coloque o salario : '))
per = str(input('Coloque a porcentagem de aumento : '))

per=float("0."+per)
print per

print ("Aumento :"+str(sal*per)+"\nNovo salario : "+str(sal+(sal*per)))
