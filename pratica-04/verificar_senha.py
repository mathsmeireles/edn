while True:
    senha = input("digite a senha (digite 'sair' para encerrar): ")
    
    if senha == "sair":
        print("encerrando...")
        break

    if len(senha) < 8:
        print("a senha deve ter 8 ou mais caracteres")
        continue

    for caractere in senha:
        if not any(caractere.isdigit()):
            print("deve ter pelo menos um número")

        #if not any(caractere.isdigit() for caractere in senha):
        #    print("deve ter pelo menos um número")


    print("senha forte")
    break
