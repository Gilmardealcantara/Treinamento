#!/usr/bin/python
#-*- coding: iso-8859-15 -*-

from Tatu import Cliente
from Tatu import Conta
from Tatu import ContaEspecial

joao = Cliente('João da Silva', '777-1234')
maria = Cliente('Maria da Silva', '777-1235')
gilmar = Cliente('Gilmar Pereira', '777-1237')


print('Nome: %s Telefone = %s' %(joao.nome, joao.telefone))
print('Nome: %s Telefone = %s' %(maria.nome, maria.telefone))
print('Nome: %s Telefone = %s' %(gilmar.nome, gilmar.telefone))


conta1 = Conta([joao], 1 , 1000)
conta2 = Conta([joao, maria], 2)
conta3 = ContaEspecial([gilmar], 3, 500, 500)

conta1.resumo()
conta2.resumo()
conta3.resumo()

