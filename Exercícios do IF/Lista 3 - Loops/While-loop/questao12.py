resposta = "nao"

while resposta == "nao" or resposta == "não":
    nome = input("Digite seu nome: ")
    resposta = input(f"Seu nome é {nome}? (sim/não): ").lower()

print(f"Dados confirmados. Olá, {nome}!")