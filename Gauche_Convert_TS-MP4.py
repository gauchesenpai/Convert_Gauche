# Gauche Convert
print ('Script feito por: t.me/Gauchesenpai\n')

import os
import subprocess

def converter_ts_para_mp4(pasta_origem, pasta_destino):
    # Certifique-se de que a pasta de destino exista
    os.makedirs(pasta_destino, exist_ok=True)

    # Itera sobre os arquivos na pasta de origem
    for arquivo in os.listdir(pasta_origem):
        if arquivo.endswith(".ts"):
            nome_arquivo = os.path.splitext(arquivo)[0]
            caminho_arquivo_ts = os.path.join(pasta_origem, arquivo)
            caminho_arquivo_mp4 = os.path.join(pasta_destino, f"{nome_arquivo}.mp4")

            # Comando FFmpeg para converter o arquivo
            comando = f'ffmpeg -i "{caminho_arquivo_ts}" -c:v copy -c:a aac "{caminho_arquivo_mp4}"'

            # Executa o comando no terminal
            subprocess.run(comando, shell=True)

if __name__ == "__main__":
    pasta_origem = input("Digite o caminho da pasta de origem (ex: C:\\Caminho\\Para\\Origem): ")
    pasta_destino = input("Digite o caminho da pasta de destino (ex: C:\\Caminho\\Para\\Destino): ")

    converter_ts_para_mp4(pasta_origem, pasta_destino)
