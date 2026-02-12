from rich import print, inspect

class Funcionario:
    # Atributos de Classe
    empresa = "Curso em Vídeo"
    def __init__(self, nome, setor, cargo):
        # Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresencao(self) -> str :
        return f":handshake: Olá, sou [blue]{self.nome.title()}[/] e sou {self.cargo.title()} do setor de {self.setor.title()} da empresa {Funcionario.empresa}"
        # self.__class__.empresa poderia substituir Funcionario.empresa
#Funcionario.empresa = "Hostnet"

c1 = Funcionario("Maria", "Administração", "Diretora")
#c1.empresa = "Estudonauta" # Cria um atributo de instancia nao de Classe
print(c1.apresencao())
#inspect(c1, all = True)

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresencao())

#inspect(Funcionario)