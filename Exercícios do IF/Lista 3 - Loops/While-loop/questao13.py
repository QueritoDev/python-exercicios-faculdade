senha_correta = "1234"
acesso = False
tentativa = 1

while tentativa<=3:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        acesso = True
        break
    else:
        print(f"Senha incorreta. Restam {3 - tentativa} tentativa(s).")
        tentativa+=1

if acesso:
    print("Acesso permitido!")
else:
    print("Acesso bloqueado!")