from rich import print

class Funcionario:
    empresa = "Curso em video"
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def apresentacao(self):
        print(f":handshake: Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}")

c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacao())

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentacao())