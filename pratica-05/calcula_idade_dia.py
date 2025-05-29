import datetime

def calcular_idades_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

idade_dias = calcular_idades_dias(2003)
print(f"sua idade aproximada em dias é: {idade_dias}")