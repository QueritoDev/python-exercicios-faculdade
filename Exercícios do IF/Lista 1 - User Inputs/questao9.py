numero = int(input("Digite um número de apenas dois algarismos: "))

while numero < 10 or numero > 99:
    numero = int(input("Digite um número de apenas dois algarismos: "))

dezenas = numero // 10
unidades = numero % 10

print(f"Algarismo das dezenas: {dezenas}")
print(f"Algarismo das unidades: {unidades}")