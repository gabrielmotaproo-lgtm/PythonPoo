from rich import print

class Livro:
    """
        cria livro e consegue passar paginas
    """
    def __init__(self, livro, qtdPagina, pagAtual = 0):
        self.livro = livro
        self.qtdPag = qtdPagina
        self.pagAtual = pagAtual
    def passarPag(self, qntsPassar):
        conta = self.qtdPag - self.pagAtual
        
        if self.pagAtual == self.qtdPag:
            print(f"Você chegou no fim do livro: página {self.pagAtual}/{self.qtdPag}")
        if conta < qntsPassar:
            self.pagAtual += conta
            print(f"Você foi pra página {self.pagAtual}. Você não consegue passar essa quantidade de páginas: {qntsPassar}")
        else:
            self.pagAtual += qntsPassar
            print(f"Você passou {qntsPassar} pag e foi pra página: {self.pagAtual}")


l1 = Livro("Tres porquin", 200)
l1.passarPag(20)
l1.passarPag(80)
l1.passarPag(101)
l1.passarPag(100)
l1.passarPag(1)
print(l1)