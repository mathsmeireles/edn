"""
Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
    valor_conta (float): O valor total da conta
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

    Retorna:
    float: O valor da gorjeta calculada
"""

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    
    return gorjeta

valor_conta = 100.00
porcentagem_gorjeta = 10.00

print(calcular_gorjeta(valor_conta, porcentagem_gorjeta))