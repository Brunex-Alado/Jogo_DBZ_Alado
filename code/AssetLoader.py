# ~~ IMPORTS ~~
import os
import sys


# ~~ FUNÇÃO PARA LOCALIZAR ARQUIVOS NO .EXE OU NO PROJETO ~~
def resource_path(relative_path):

    try:
        # ~~ PYINSTALLER CRIA PASTA TEMPORÁRIA ~~
        base_path = sys._MEIPASS
    except Exception:
        # ~~ EXECUÇÃO NORMAL DO PROJETO ~~
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)