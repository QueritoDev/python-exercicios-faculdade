numero = 0.0
positivos = 0

for i in range (1, 11):
    numero = float(input(f"Digite o {i}º numero: "))
    if(numero<0.0):
        positivos+=1

print(f"Quantidade de numeros positivos: {positivos}")
