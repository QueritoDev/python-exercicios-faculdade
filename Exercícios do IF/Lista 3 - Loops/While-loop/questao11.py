saldo = 1500
continuar = "s"

while continuar == "s":
    print(f"Saldo atual: R$ {saldo:.2f}")
    saque = float(input("Valor do saque: R$ "))

    if saque > saldo:
        print("Operação não pode ser realizada: saldo insuficiente.")
    else:
        saldo -= saque
        print(f"Saque realizado! Novo saldo: R$ {saldo:.2f}")

    continuar = input("Deseja fazer outro saque? (s/n): ").lower()