from rich import print
from rich.panel import Panel
caixa = Panel("Esse aqui é um painel de exemplo :+1:", title="Mensagem", style="red",width=len("Esse aqui é um painel de exemplo :+1:")+2)
print(caixa)
caixa2 = Panel(f"Esse aqui é outro exemplo de painel",title="titulo",title_align="left",subtitle="titulo2",expand=True)
print(caixa2)