def is_palindromo(texto):
    texto_limpo = ''.join(char.lower()
                          for char in texto
                          if char.isalnum())
    
    return texto_limpo == texto_limpo[::-1]

expressao = "asa"
resultado = is_palindromo(expressao)

if resultado == True:
    resposta = "sim"
else:
    resposta = "não"

print(f"a {expressao} é um palindromo? {resposta}")
