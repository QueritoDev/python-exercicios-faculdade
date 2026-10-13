# 6. Dada uma quantidade de horas, exibir o valor equivalente em 
# minutos e em segundos.

horas = float(input("Digite a hora: "))
minutos = horas * 60
segundos = horas * 3600

print(f"{horas:.0f} hora(s) equivale a: ")
print(f"- {minutos:.0f} minutos")
print(f"- {segundos:.0f} segundos")