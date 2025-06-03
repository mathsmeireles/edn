import csv

def escrever_csv(nome_arquivo, dados):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Nome', 'Idade', 'Cidade'])
        for linha in dados:
            escritor.writerow(linha)
    print(f'dados salvos em {nome_arquivo}')


dados = [
    ['Anna', 24, 'Rio de Janeiro'],
    ['Bento', 30, 'São Paulo'],
    ['José', 20, 'Vitória']
]

if __name__ == "__main__":
    nome_arquivo = input("digite o nome do arquivo csv: ")
    escrever_csv(nome_arquivo, dados)