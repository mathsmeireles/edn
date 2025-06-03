import pandas as pd

def processar_log_treinamento(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        desvio_padrao_tempo = df['tempo_execucao'].std()
        media = df['tempo_execucao'].mean()
        print(f"DP: {desvio_padrao_tempo:.2f}")
        print(f"Média: {media:.2f}")
    except FileNotFoundError:
        print("arquivo não encontrado")
    except Exception as e:
        print(f"erro ao processar o arquivo de log")
        
nome_arquivo = input("digite o nome do arquivo de log: ")
processar_log_treinamento(nome_arquivo)
