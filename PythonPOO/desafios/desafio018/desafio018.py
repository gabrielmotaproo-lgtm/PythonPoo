from rich import print
from rich.panel import Panel

class Churrasco:


    def __init__(self, nome, quantidade, precoKg=82.40, consumoPadrao=0.4): #Construtor
        self.nome = nome
        self.qtd = quantidade
        self.precoKg = precoKg
        self.consumoPadrao = consumoPadrao
    def analisar(self):
        comprarKg = self.consumoPadrao * self.qtd
        comprarCusto = comprarKg * self.precoKg
        pessoaPaga = comprarCusto / self.qtd
        conteudo = f"Analisando [green]{self.nome}[/] com [blue]{self.qtd} convidados[/] \n Cada participante comerá {self.consumoPadrao}Kg e cada Kg custa {self.precoKg}\n Recomendo [blue]comprar {comprarKg}Kg de carne[/] \n O custo total será de [green]R${comprarCusto:,.2f}[/]\n Cada pessoa pagará [yellow]R${pessoaPaga} para participar.[/]"
        panel = Panel(conteudo, title=self.nome)
        print(panel)


c1 = Churrasco("Churras do CPX", 100)
c1.analisar()
#Considere:
# Consumo padrão: 400g por pessoa
# Preço: R$82,40/Kg

print(c1)