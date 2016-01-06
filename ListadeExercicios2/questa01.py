print ('Coloque os lados de Triangulo: ')
l1 = input()
l2 = input()
l3 = input()

#ver se e possivel exir um tiandulo 
#um lado deve nao pede ser maior q a soma dos outros dois

if l1 >= l2+l3 or l2 >= l1+l3 or l3 >= l2+l1 : 
	print ('Nao e possivel que haja um triangulo')
	exit()
#ver que tipo de triandulo

print 'E possivel formar um triangulo : '
if l1==l2 and l2==l3 : 
	print ('Equilatero.')
elif l1==l2 or l2==l3 or l3==l1 :
	print ('isoceles.')
else : 
	print ('Escaleno')
