"""
Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
- Valor em reais: R$ 100.00
- Taxa do dólar: R$ 5.70
- Taxa do euro: R$ 6.40
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

valor_reais = 100.00
taxa_dolar = 5.70
taxa_euro = 6.40

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f"R${valor_reais}")
print("$", round(valor_dolar))
print("€", round(valor_euro))