import json

def ler_json(nome_arquivo):
    try:
        with open (nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            print(dados)
    except FileNotFoundError:
        print("arquivo não encontrado")

def escrever_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json)
        print(f"dados salvos em {nome_arquivo}")
    except Exception as e:
        print(f"erro ao salvar o arquivo: {e}")



dados = {
    "nome": "João",
    "idade": 25,
    "cidade": "Vitória"
}

if __name__ == "__main__":
    nome_arquivo = input("digite o nome do arquivo json: ")
    escrever_json(nome_arquivo, dados)
    ler_json(nome_arquivo)