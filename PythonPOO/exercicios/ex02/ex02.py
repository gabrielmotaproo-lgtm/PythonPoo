class Pessoa:
    """
    Essa classe cria uma pessoa
    """
    # Método Construtor
    def __init__(self, n="", i=0):
        self.nome = n
        self.altura = 0
        self.idade = i
        self.fome = True
    # Método de Instância
    def comer(self):
        self.fome = False
    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos e fome: {self.fome}"
    
g1 = Pessoa("Gabriel", 18)
g1.comer()
print(g1.mensagem())



g2 = Pessoa("Gabriela", 18)
print(g1.mensagem())
print(Pessoa.__doc__)
