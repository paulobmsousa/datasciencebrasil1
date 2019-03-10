from testecliente import Cliente
from testeconta import Conta

cliente1 = Cliente('Gui', '123456789-10', 27)
conta1 = Conta(cliente1, 10.5, 1000)
print(conta1.consultarSaldo())
conta1.depositar(1000.40)
print(conta1.consultarSaldo())
conta1.sacar(500)
print(conta1.consultarSaldo())
conta1.sacar(1000)
print(conta1.consultarSaldo())
