# Declaração de Classe
class Gafanhoto:

    def __init__(self): # Metodo construtor
        # Atributos de instância
        self.idade = 0
        self.nome = ""

    # Métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome.title()} é gafanhoto(a) e tem {self.idade} anos de idade"

# Declaração de Objeto
g1 = Gafanhoto()
g1.nome = "lucas"
g1.idade = 22
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Alice"
g2.idade = 24
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())


