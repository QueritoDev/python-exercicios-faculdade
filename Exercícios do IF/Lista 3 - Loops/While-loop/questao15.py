saldo = 1000
opcao = ""

while opcao != "4":
    print("\n1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == "2":
        valor = float(input("Valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            print("Depósito realizado!")
        else:
            print("Valor inválido.")
    elif opcao == "3":
        valor = float(input("Valor do saque: R$ "))
        if valor <= 0:
            print("Valor inválido.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            print("Saque realizado!")
    elif opcao != "4":
        print("Opção inválida!")

print("Obrigado por usar o caixa eletrônico.")