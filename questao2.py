#Maior de três
numero1 = int(input("Digite o 1 º número: "))
numero2 = int(input("Digite o 2 º número: "))
numero3 = int(input("Digite o 3 º número: "))

maior = 0

if (numero1>numero2) and (numero1>numero3):
    maior = numero1

elif(numero2>numero1) and (numero2>numero3):
    maior = numero2
else:
    maior = numero3

print(f"O número maior é {maior}")