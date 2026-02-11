# Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto que é uma pessoa que tem nome e idade

    Para criar uma nova pessoa use:
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "", idade = 0): # Metodo construtor
        # Atributos de instância
        self.idade = idade # self.atributo = parametro
        self.nome  = nome


    # Métodos de instância
    def aniversario(self):
        self.idade += 1
    def __str__(self):
        return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade"
    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

# Declaração de Objeto
g1 = Gafanhoto("Lucas", 21)
g1.aniversario()

print(g1)
print(g1.__dict__) #Attribute
print(g1.__getstate__()) #Method é personalizável
print(g1.__class__)
print(g1.__doc__) #Docstring
#DUNDER = Double Underline __