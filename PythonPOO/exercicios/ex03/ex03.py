class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome 
        self.saldo = saldo
    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo"
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depositou {valor}")
    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque NEGADO {valor:,.2f}. Saldo insuficiente")
        else:
            self.saldo -=  valor
            print(f"Saque efetuado: {valor}")

c1 = ContaBancaria(260, "Gabriel", 680.64)
print(c1)
c1.depositar(19.36)
print(c1)
c1.sacar(2700)
print(c1)
