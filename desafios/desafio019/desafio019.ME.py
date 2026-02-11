from rich import print
class Livro:
    def __init__(self,titulo,paginas):
        self.titulo = titulo.title()
        self.paginas = paginas
        print(f"Você acabou de abrir o livro {self.titulo} que tem {self.paginas} paginas. \nVocê agora está na página 1.")

    def avancar_paginas(self,n):
        for p in range(1,n+1):
            if p > self.paginas:
                break
            print(f"Pág{p+1} -> ",end="")
        print(f"Você avançou {n} página(s) e está na página {p+1}")

l1 = Livro("10 coisas que aprendi",20)
l1.avancar_paginas(1)
l1.avancar_paginas(2)