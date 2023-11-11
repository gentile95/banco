class Conta:
    
    saldo = 0
    limite_saque = 3
    limite_valor_saque = 500
    quantidade_saques = 0
    extrato = []
    acao = []

    def __init__(self, numero_conta, cpf_cliente):
        self.numero_conta = numero_conta
        self.cpf_cliente = cpf_cliente

    def sacar(self, valor):
        if self.quantidade_saques < self.limite_saque:
            if valor <= 500:
                if valor <= self.saldo:
                    saldo_anterior = self.saldo
                    self.saldo -= valor
                    self.quantidade_saques += 1
                    self.extrato.append(f"Saldo anterior: {saldo_anterior}\nSaque de: {valor}\nNovo saldo: {self.saldo}")
                else:
                    print("Saldo insuficiente")
            else:
                print("Valor não permitido. Limite de 500,00")
        else:
            print("Quantidade máxima de saques atingida. Limite de 3")

    def mostrar_extrato(self):
        print("\n".join(self.extrato))
    
    def depositar(self, valor):
        saldo_anterior = self.saldo
        self.saldo += valor
        self.extrato.append(f"Saldo anterior: {saldo_anterior}\nDepósito de: {valor}\nNovo saldo: {self.saldo}")

            


    