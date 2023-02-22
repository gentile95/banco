def depositar(deposito):
  saldo += deposito
  deposito_count += 1
  acao.append(f"depósito_{deposito_count} R$ +{deposito:.2f}")
  extrato.append(f"total R$ {saldo:.2f}")
  print("\nQuantia depositada!\n")
  return saldo

def saque(valor):
  saque_count += 1
  saldo -= valor
  acao.append(f"saque_{saque_count} R$ -{valor:.2f}")
  extrato.append(f"total R$ {saldo:.2f}")
  return saldo

def extrato():
  extrato_dic = {k:v for k, v in zip(acao, extrato)}
  mostrar_extrato = "\n".join(f"{key} : {value}" for key, value in extrato_dic.items())
  print(f"""\nSeu extrato atualizado:

-----------------------
{mostrar_extrato}
-----------------------
""")