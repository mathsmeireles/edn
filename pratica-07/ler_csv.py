import csv

def ler_csv(nome_arquivo):
    with open(nome_arquivo, 'r', newline='') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            print(linha)


if __name__ == "__main__":
    nome_arquivo = input("digite o nome do arquivo: ")
    ler_csv(nome_arquivo)