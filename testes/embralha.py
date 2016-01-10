

def embaralha(s) :
	import random
	lista=list(s)
	random.shuffle(lista)
	return  ''.join(lista)



s = raw_input('Cloque a string : ')

print embaralha(s)
