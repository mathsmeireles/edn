def calcular_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final

preco = 100
desconto = 10

preco_final = calcular_desconto(preco, desconto)

print(f"o preço final com {desconto}% de desconto é R${preco_final}")
