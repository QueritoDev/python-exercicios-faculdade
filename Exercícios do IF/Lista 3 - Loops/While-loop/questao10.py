opcao = ""

while opcao != "5":
    print("\n1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opcao = input("Escolha: ")

    if opcao in ["1", "2", "3", "4"]:
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))

        if opcao == "1":
            print(f"Resultado: {a + b}")
        elif opcao == "2":
            print(f"Resultado: {a - b}")
        elif opcao == "3":
            print(f"Resultado: {a * b}")
        else:
            if b == 0:
                print("Não é possível dividir por zero.")
            else:
                print(f"Resultado: {a / b}")
    elif opcao != "5":
        print("Opção inválida!")

print("Programa encerrado.")