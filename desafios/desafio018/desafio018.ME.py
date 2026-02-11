from rich import print
from rich.panel import Panel

def formatoContabil(n):
    return f"R${n:,.2f}"

class Churrasco:
    def __init__(self,titulo,quant,):
        self.titulo = titulo
        self.quant = quant

    def analisar(self):
        consumoMedio = 0.4
        precoCarne = 82.40
        qtdCarne = self.quant*consumoMedio
        custoTotal = qtdCarne*precoCarne
        custoIndividual = custoTotal/self.quant
        print(Panel(title=self.titulo,
        renderable=f"""Analisando [green]{self.titulo}[/] com [blue]{self.quant}[/] convidados
Cada participante comerá {consumoMedio}Kg e cada Kg custa {formatoContabil(precoCarne)}
Recomendo [blue]comprar {qtdCarne:.1f}Kg[/] de carne
O custo total será de [green]{formatoContabil(custoTotal)}[/]
Cada pessoa pagará [yellow]{formatoContabil(custoIndividual)}[/] para participar."""))

c1 = Churrasco("Churrsasco dos amigos",15)
c1.analisar()

# CONSIDERE:
# Consumo padrão: 400g/pessoa
# Preço: R$82,40/Kg