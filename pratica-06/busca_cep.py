import requests


def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        if "erro" in dados:
            return "cep inválido"
        return f"""
        cep = {dados['cep']}
        logradouro = {dados['logradouro']}
        bairro = {dados['bairro']}
        cidade = {dados['localidade']}
        estado = {dados['uf']}    
        """
    except requests.RequestException as e:
        return f"erro na consulta {e}"


def main():
    cep = int(input("digite o cep (somente números): "))
    print("consultando cep")
    resultado = consulta_cep(cep)
    print(resultado)


if __name__ == "__main__":
    main()