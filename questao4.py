#Calculadora

numero1 = float(input("Digite o primeiro número que deseja: "))
numero2 = float(input("Digite o segundo número que deseja: "))
resultado = float
operador = input("Digite o operador desejado para realizar a operação: ")

if operador=="+":
    resultado = numero1 + numero2
elif operador=="-":
    resultado = numero1 - numero2
elif operador=="/":
    resultado = numero1 / numero2
elif operador=="*":
    resultado = numero1 * numero2

print(f"Resultado da operação: {resultado}")