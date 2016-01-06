print ('Coloque as quantidades no dos intens pedidos.')
dias = int(input('Dias: '))
horas = int (input('Horas: ')) 
minutos = int (input('Minutos: ')) 
seg = int(input('Segundos: ')) 

total_seg=seg + minutos*60 + horas*60*60 + dias*24*60*60

print "Total de Segundos = " + str(total_seg)
