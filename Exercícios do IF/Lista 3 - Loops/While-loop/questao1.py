print("== Tela de Registro ==\n")
username = input("Digite o nome de usuario: ")
senha = input("Digite a senha de usuario: ")

print("\n== Tela de Login ==\n")
verificaNome = input("Digite o nome de usuário: ")
verificaSenha = input("Digite a senha de usuario: ")

while(verificaNome!=username and verificaSenha!=senha):
    print("Dados incorretos! Tente novamente!")
    verificaNome = input("Digite o nome de usuário: ")
    verificaSenha = input("Digite a senha de usuario: ")

if(verificaNome==username and verificaSenha==senha):
    print("Login feito com sucesso\n")
    print(f"Bem vindo {username}!")
    

