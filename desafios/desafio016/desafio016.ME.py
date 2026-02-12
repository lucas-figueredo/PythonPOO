from rich import print,inspect


class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresencao(self):
        return f":handshake: Olá, sou {self.nome.title()} e sou {self.cargo.title()} do setor de {self.setor.title()} da empresa Curso em vídeo"


c1 = Funcionario("Maria", "Administração", "Diretora")
#print(c1.apresencao())
inspect(c1,methods=True)

c2 = Funcionario("Pedro", "TI", "Programador")
#print(c2.apresencao())
inspect(c2)