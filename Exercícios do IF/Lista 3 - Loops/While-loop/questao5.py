total = 0

while total < 1000:
    deposito = float(input("Valor do depósito: R$ "))
    total += deposito

print(f"Meta atingida! Total acumulado: R$ {total:.2f}")