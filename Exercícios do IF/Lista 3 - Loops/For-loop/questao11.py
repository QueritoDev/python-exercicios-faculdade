numero = 0
maior = 0

for i in range (1, 6):
    numero = int(input(f"Digite o {i}º numero: "))
    if(numero > maior):
        maior = numero

print(f"\nO maior numero foi: {maior}")