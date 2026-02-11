from rich import print
from rich import inspect
#inspect(int, all=True)
print(int("01",2))

class ContaBancaria:
    """
    Cria uma conta bancária que permite realizar saques e depósitos
    """
    def __init__(self, id, titular, saldo):
        self.id = id
        self.titular = titular.title()
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. saldo atual de R${self.saldo:,.2f}")


    def __str__(self):
        return f"A conta {self.id} de {self.titular} possui R${self.saldo:,.2f} de saldo."

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")
        else:
            print(f"Saque de R${valor:,.2f} NÃO autorizado na conta {self.id}: SALDO INSUFICIENTE")

c = ContaBancaria(111,"josé", 500)
inspect(c)
#print(c.__getstate__())