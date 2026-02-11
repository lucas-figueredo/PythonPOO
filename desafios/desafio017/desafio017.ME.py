from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self,nome, preco):
        self.nome = nome.title()
        self.preco = f"R${preco:,.2f}"

    def etiqueta(self):
         print(Panel(f"{self.nome:^40}\n{40*"-"}\n{self.preco:.^40}",title="Produto",expand=False))

p1 = Produto("iphone 17 Pro max",25_000.85)
p2 = Produto("Notebook gamer", 8_000)
p3 = Produto("Mouse",120)

p1.etiqueta()
p2.etiqueta()
p3.etiqueta()
