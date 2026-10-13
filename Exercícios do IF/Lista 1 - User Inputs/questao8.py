deposito = float(input("Digite o valor do depósito: "))
taxa = float(input("Digite a taxa de juros mensal: "))
tempo = int(input("Digite a quantidade de meses: "))

total = deposito * ((1 + (taxa / 100)) ** tempo)
rendimento = total - deposito

print(f"Valor do rendimento: R$ {rendimento:.2f}")
print(f"Valor total após o rendimento: R$ {total:..2f}")