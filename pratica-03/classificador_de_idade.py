""""
2- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais).
"""

idade = 22

if idade >= 0 and idade < 13: # 0-12
    print("criança")
elif idade < 18:
    print("adolescente") # 13-17
elif idade < 60:
    print("adulto") # 18-59
else:
    print("idoso") # 60+