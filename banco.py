from classes.conta import Conta

conta = Conta(51248, '12345678910')

def main():

    while(True):

        print("""
        Selecione a opção desejada:
    
        1 - Depositar
        2 - Sacar
        3 - Extrato 
        4 - Sair 
        ---------------------------
    
        """)

        valido = False
        while (valido == False):
            try:
                x = int(input())
                valido = True
            except ValueError as e:
                print("Valor não é válido, digite uma nova opção")
            
        if x < 1 or x > 4:
            print("Opção inválida")
            continue
        else:
            match(x):
                case 1:
                    print("Valor do depósito: ")
                    deposito = float(input())
                    conta.depositar(deposito)
                case 2:
                    print("Valor do saque: ")
                    saque = float(input())
                    conta.sacar(saque)
                case 3:
                    conta.mostrar_extrato()
                case 4:
                    break

if __name__ == '__main__':
    main()