print("== Tela de Registro de Conta ==")
username = input("Digite o nome de usuario: ")
senha = input("Digite a senha: ")

print("== Tela de Login ==")
verificarName = input("Digite o nome de usuario:")
verificarSenha = input("Digite a senha: ")

while(verificarName!=username and verificarSenha!=senha):
    print("Dados incorretos! Tente novamente\n")
    verificarName = input("Digite o nome de usuario:")
    verificarSenha = input("Digite a senha: ")

if(verificarName==username and verificarSenha==senha):
    print(f"Login feito com sucesso! Bem vindo {username}!")

