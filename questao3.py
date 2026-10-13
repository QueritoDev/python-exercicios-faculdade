#Calculo IMC

peso = float(input("Digite o peso em KG: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura * altura)



print(f"IMC: {imc}")
print("Classificação: ")