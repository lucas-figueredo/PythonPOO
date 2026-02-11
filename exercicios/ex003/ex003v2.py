from rich import print
from rich import inspect

class ContaBancaria:
    """
    Cria uma conta bancária que permite realizar saques e depósitos
    """
    def __init__(self, id, titular, saldo):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. saldo atual de R${self.saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} possui R${self.saldo:,.2f} de saldo."

    def __getstate__(self):
        return f"Estado: id = {self.id}; titular = {self.titular}; saldo = R${self.saldo:,.2f}"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} [bold green]autorizado[/] na conta {self.id}")

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} [bold green]autorizado[/] na conta {self.id}")
        else:
            print(f"Saque de R${valor:,.2f} [bold red]NEGADO[/] na conta {self.id}: SALDO INSUFICIENTE")



c1 = ContaBancaria(112, "Gustavo", 10000)
c1.depositar(500)
c1.sacar(2_000_000)
print(c1)
print(c1.__getstate__())
inspect(c1)
#print(c1.__doc__)
#OBS: o ideal é que não haja prints dentro de métodos