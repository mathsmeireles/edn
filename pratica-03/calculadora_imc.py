"""
3- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso" 

< 25: classificacao = "Peso normal"

 < 30: classificacao = "Sobrepeso"

 Para os demais cenários: classificacao = "Obeso"
"""

peso = 56.5
altura = 1.75

imc = peso / (altura ** 2)

print(f"imc: {imc:.2f}")
if imc < 18.5:
    print("abaixo do peso")
elif imc < 25:
    print("peso normal")
elif imc < 30:
 print("sobrepeso")
else:
   print("obeso")