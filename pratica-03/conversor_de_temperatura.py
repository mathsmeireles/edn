"""
4- Conversor de Temperatura Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

origem = "celsius"
destino = "fahrenheit"
valor = 28


if origem == "celsius":
    celsius = valor
elif origem == "fahrenheit":
    celsius = (valor - 32) * 5/9
elif origem == "kelvin":
    celsius = valor - 273.15
else:
    raise ValueError("Unidade de origem inválida.")



if destino == "celsius":
    print(celsius)
elif destino == "fahrenheit":
    print((celsius * 9/5) + 32)
elif destino == "kelvin":
    print(celsius + 273.15)
else:
    raise ValueError("Unidade de destino inválida.")