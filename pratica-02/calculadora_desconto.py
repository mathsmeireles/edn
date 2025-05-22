"""
Calculadora de Desconto Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

- Nome do produto: "Camiseta"
- Preço original: R$ 50.00
- Porcentagem de desconto: 20% O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nome_produto = "camisa"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print("produto:", nome_produto)
print(f"preço original R${preco_original:.2f}")
print(f"desconto: {porcentagem_desconto}%")
print(f"valor desconto R${valor_desconto:.2f}")
print(f"preço final R$ {preco_final}")