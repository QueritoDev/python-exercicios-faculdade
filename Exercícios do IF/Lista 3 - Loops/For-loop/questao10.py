#Peça ao usuário para digitar uma palavra e informe quantas vogais existem nela

texto = str(input("Digite uma palavra: "))
vogais = "aeiouAEIOU"

contador = 0

for letra in texto:
    if letra in vogais:
        contador +=1

print(f"Quantidade de vogais na palavra {texto}: {contador} vogais")