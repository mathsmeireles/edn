"""
Calculadora de Soma com Entrada do Usuário

Leia 2 valores inteiros e armazene-os nas variáveis `A` e `B`. Efetue a soma de `A` e `B`, atribuindo o seu resultado à variável `X`. 

Entrada: 
A entrada contém 2 valores inteiros informados pelo usuário. 

Saída:
Imprima a mensagem `"X = "` (letra X maiúscula) seguido pelo valor da variável `X` e pelo final de linha.
"""

A = int(input("insira o primeiro número: "))
B = int(input("insira o segundo número: "))

X = A + B

print(f"X = {X}")