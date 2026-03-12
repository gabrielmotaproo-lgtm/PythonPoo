from rich import print
from rich.panel import Panel


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def etiqueta(self):
        panel = Panel(f"{self.nome:^30}\n{"":-^30}\n{self.preco:.^30,.2f}",title="Produto",width=35)
        print(panel)

p1 = Produto("Produto 1", 40)
p2 = Produto("Produto 2", 20)

p1.etiqueta()
p2.etiqueta() 