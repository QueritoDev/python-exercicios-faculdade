votos1 = 0
votos2 = 0
votos3 = 0
opcao = ""

while opcao != "0":
    print("\n1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    print("0 - Encerrar votação")
    opcao = input("Seu voto: ")

    if opcao == "1":
        votos1 += 1
    elif opcao == "2":
        votos2 += 1
    elif opcao == "3":
        votos3 += 1
    elif opcao != "0":
        print("Opção inválida!")

print("\n--- Resultado ---")
print(f"Candidato 1: {votos1} voto(s)")
print(f"Candidato 2: {votos2} voto(s)")
print(f"Candidato 3: {votos3} voto(s)")