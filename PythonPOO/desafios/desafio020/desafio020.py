from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []
    def add_favoritos(self, jogo, ):
        self.favoritos.append(jogo)
        print(f"jogo adicionado aos favoritos {jogo}")
    def ficha(self):
        panel = Panel(f"Nome real: {self.nome} \nJogos favoritos:\n{self.favoritos}")
        print(panel)
j1 = Gamer("Gabriel", "Mota")
j1.add_favoritos("Fortnite")
j1.add_favoritos("Forza")
j1.ficha()

j2 = Gamer("Gabriela", "gabiimrds")
j2.add_favoritos("Fifa")
j2.add_favoritos("Clash Royale")
j2.ficha()
print(j1)
print(j2)

