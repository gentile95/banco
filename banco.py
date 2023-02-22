import functions

LIMITE_SAQUE = 3
MAX_SAQUE = 500
saldo = 1000
acao = []
extrato = []
saque_count = 0
deposito_count = 0

while (True):
  print("""
  Selecione a opção desejada:

  1 - Depositar
  2 - Sacar
  3 - Extrato 
  4 - Sair 
  ---------------------------

  """)

  x = int(input())

  if x < 1 or x > 4:
    print("\nOpção inválida")
  else:
    if x == 1:
      print("\nInforme a quantia a ser depositada: ")
      deposito = float(input())
      if deposito < 0:
        print("\nValor digitado incorretamente")
      else:
        functions.depositar(deposito)
    
    elif x == 2:
      if saque_count < 3:
        print("\nQual valor a ser sacado?")
        saque = float(input())
        if saque < 0:
          print("\nValor digitado incorretamente")
        else:
          if saque > MAX_SAQUE:
            print("\nDesculpe, o limite máximo para saque é de R$ 500.00")
          else:
            if saldo < saque:
              print("\nDesculpe, não há saldo suficiente para essa transação")
            else:
              functions.saque(saque)
      else:
        print("\nDesculpe, você atingiu o limite máximo de saque")
    
    elif x == 3:
      if saque_count == 0 and deposito_count == 0:
        print("\nAinda não foi realizada nenhuma ação")
      else:
        functions.extrato()
    
    else:
      break


