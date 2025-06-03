import json
import requests

def obter_usuario_aleatorio():
    url = 'https://randomuser.me/api/'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        return f"nome: {nome}\nemail: {email}\npaís: {pais}"
    except requests.RequestException:
        return f"erro ao obter o usuário"

print("gerando usuário aleatório")
usuario = obter_usuario_aleatorio()
print(usuario)