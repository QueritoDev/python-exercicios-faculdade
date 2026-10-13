prova1 = float(input("Digite a nota da prova 1"))
prova2 = float(input("Digite a nota da prova 2"))
prova3 = float(input("Digite a nota da prova 3"))

peso1 = 2
peso2 = 3
peso3 = 5
media_pond = (prova1 * peso1) + (prova2 * peso2) + (prova3 * peso3) / peso1 + peso2 + peso3

print(f"A média ponderada é {media_pond:.2f}")