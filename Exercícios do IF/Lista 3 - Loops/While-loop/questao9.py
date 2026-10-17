import random

secreto = random.randint(1, 50)
palpite = 0
tentativas = 0

while palpite != secreto:
    palpite = int(input("Seu palpite (1 a 50): "))
    tentativas += 1

    if palpite < secreto:
        print("Muito baixo! Tente um número maior.")
    elif palpite > secreto:
        print("Muito alto! Tente um número menor.")

print(f"Acertou em {tentativas} tentativas!")