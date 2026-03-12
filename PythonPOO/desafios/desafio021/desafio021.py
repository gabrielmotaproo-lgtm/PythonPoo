from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampada = True
    def destampar(self):
        self.tampada = False
    def escrever(self, texto):
        if self.tampada == True:
            print("Destampe a caneta para escrever")
        elif self.cor == "vermelha":
            print(f"[red]{texto}[/]")
        elif self.cor == "azul":
            print(f"[blue]{texto}[/]")
        elif self.cor == "verde":
            print(f"[green]{texto}[/]")
c1 = Caneta("vermelha")
c2 = Caneta("azul")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()


c1.escrever("Olá, tudo bem")
c2.escrever("Olá Gafanhoto!")
c3.escrever("Vamos exercitar")