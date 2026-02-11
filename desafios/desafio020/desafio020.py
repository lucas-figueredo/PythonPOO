from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick
        self.jogos = list()

    def add_favoritos(self,j):
        self.jogos.append(j)

    def mostrar_favoritos(self):
        for i in self.jogos:
            print(f":video_game: [blue]{i}[/]")

    def ficha(self):
        print(Panel(title=f"Jogador <{self.nick}>",
              renderable=f"""nome real: [black on Blue]{self.nome}[/]
Jogos Favoritos:"""))

j1 = Gamer("Fabricio da Silva","Detonator2025")
j1.add_favoritos("crash")
j1.ficha()


