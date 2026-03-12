class Pessoa:
    # Método Construtor
    def __init__(self):
        self.nome = ""
        self.altura = 0
        self.idade = 0
        self.fome = True
    # Método de Instância
    def comer(self):
        self.fome = False
    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos e fome: {self.fome}"
    
g1 = Pessoa()
g1.nome = "Gabriel"
g1.idade = 18
g1.comer()
print(g1.mensagem())

g2 = Pessoa()
g2.nome = "Gabriela"
g2.idade = 18
print(g1.mensagem())