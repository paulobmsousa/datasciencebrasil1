class Conta:
	def __init__ (self, cliente, saldo, limite):
		self.cliente = cliente
		self.saldo = saldo
		self.limite = -limite
	
	def depositar (self, quant):
		if (quant>0):
			self.saldo += quant
			print('Depositado: '+str(quant))
		else:
			print('Erro no deposito')
	
	def consultarSaldo (self):
		return self.saldo
	
	def sacar (self, quant):
		if (self.saldo-quant<self.limite):
			print('Erro: saldo insuficiente')
		else:
			self.saldo -= quant
			print('Sacado: '+str(quant))
	