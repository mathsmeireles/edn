"""
Crie um programa que permita a um professor registrar as
notas de uma turma. O programa deve continuar solicitando
notas até que o professor digite 'fim'. Notas válidas são de 0 a
10. O programa deve ignorar notas inválidas e continuar
solicitando. No final, deve exibir a média da turma.
"""

lista_notas = []
while True:
    try:
        entrada = input("digite uma nota ou digite: 'fim' para encerrar: ")
        if entrada.lower() == "fim":
            break
        nota = float(entrada)
        if 0 <= nota <= 10:
            lista_notas.append(nota)
        else:
            print("nota inválida: digite um valor entre 0 e 10")
    except ValueError:
        print("entrada inválida")

if lista_notas:
    media = sum(lista_notas)
    print(f"\na média da turma é {media}")
    print(f"o total de notas válidas é: {len(lista_notas)}")
else:
    print("nenhuma nota foi registrada")
