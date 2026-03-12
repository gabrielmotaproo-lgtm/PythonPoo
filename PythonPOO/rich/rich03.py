from rich import print
from rich.table import Table

tabela = Table(title="Tabela Preços")

tabela.add_column("Nome")
tabela.add_column("Preço")
tabela.add_row("Lápis", "R$1,50")                                        


print(tabela)