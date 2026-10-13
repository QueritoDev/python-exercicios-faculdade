numero = input("Digite um número de apenas três algarismos: ")

while len(numero)<3 or len(numero) > 3:
    numero = int(input("Digite um número de apenas três algarismos: "))

numero_invertido = numero[::-1]
print(f"Número digitado: {numero}")
print(f"Número invertido: {numero_invertido}")