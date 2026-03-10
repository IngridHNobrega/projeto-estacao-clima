import sys
ARQUIVO = "dados/temperatura.txt"

def validar_temperatura(valor):
    try:
        temperatura = float(valor)

        if temperatura < -90 or temperatura > 60:
            print(f"Erro: temperatura impossível detectada: {temperatura}")
            return False

        return True

    except ValueError:
        print(f"Erro: valor inválido encontrado: {valor}")
        return False


def verificar_arquivo():

    try:
        with open(ARQUIVO, "r") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            valor = linha.strip()

            if not validar_temperatura(valor):
                sys.exit(1)

        print("Todos os dados estão válidos!")

    except FileNotFoundError:
        print("Arquivo de temperatura não encontrado")
        sys.exit(1)


if __name__ == "__main__":
    verificar_arquivo()
