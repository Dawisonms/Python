import os

# Defina o diretório que você deseja verificar
diretorio_alvo = "C:"

# Verifique se o diretório existe
if os.path.exists(diretorio_alvo):
    # Liste todos os arquivos no diretório
    lista_arquivos = os.listdir(diretorio_alvo)

    # Imprima os nomes dos arquivos
    print("Arquivos no diretório:")
    for arquivo in lista_arquivos:
        print(arquivo)
else:
    print(f"O diretório '{diretorio_alvo}' não existe.")
