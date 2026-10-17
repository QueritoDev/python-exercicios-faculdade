continuar = "s"

while continuar == "s":
    celsius = float(input("Temperatura em Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius}°C = {fahrenheit:.1f}°F")
    continuar = input("Deseja converter outra? (s/n): ").lower()