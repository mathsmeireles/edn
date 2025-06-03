import requests
from datetime import datetime

def conversor_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        cotacao = dados[f"{moeda}BRL"]
        return f"""
        moeda {moeda} para BRL
        valor atual R${float(cotacao["bid"]):.2f}
        máxima R${float(cotacao["high"]):.2f}
        mínima R${float(cotacao["low"]):.2f}
        data e hora: {datetime.fromtimestamp(int(cotacao['timestamp']))}
        """
    except requests.RequestException as e:
        return f"erro ao obter cotação {e}"

moeda = input("digite o código da moeda para cotação (ex: USD, EUR, GBP): ").upper()
print("obtendo dados")
resultado = conversor_moeda(moeda)
print(resultado)