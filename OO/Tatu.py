#!/usr/bin/python
#-*- coding: iso-8859-15 -*-

class Cliente: 
	def __init__(self, nome, telefone):
		self.nome = nome 
		self.telefone = telefone

class Conta:
	def __init__(self, clientes, numero, saldo = 0): 
		self.saldo = saldo
		self.clientes = clientes
		self.numero = numero 
	def resumo(self):
		print("CC Número: %s Saldo: %10.2f" %(self.numero, self.saldo))
	def saque(self, valor):
		if self.saldo >= valor:
			self.saldo -=  valor
	def deposit(self, valor) :
		self.saldo += valor

class ContaEspecial(Conta) : 
	def __init__(self, clientes, numero, saldo=0,  limite=0):
		Conta.__init__(self, clientes, numero,saldo)
		self.limite = limite
	def saque(self, valor):	
		if self.saldo + self.limite >= valor:
			self.saldo -= valor
	def resumo(self):
		print("CCE Número: %s Saldo: %10.2f Limite: %10.2f" %(self.numero, self.saldo, self.limite))
	




