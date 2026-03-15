import sqlite3


# ~~ CLASSE DE ACESSO AO BANCO DE DADOS SQLITE ~~
class DBProxy:

    def __init__(self, db_name: str):

        # ~~ CONEXÃO COM O BANCO DE DADOS ~~
        self.connection = sqlite3.connect(db_name)

        # ~~ CRIAÇÃO DA TABELA DE SCORE CASO NÃO EXISTA ~~
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS score(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                score INTEGER NOT NULL,
                date TEXT NOT NULL
            )
            """
        )


    # ~~ SALVAR SCORE NO BANCO ~~
    def save(self, score: int, date: str):

        self.connection.execute(

            "INSERT INTO score (score, date) VALUES (?, ?)",

            (score, date)
        )

        self.connection.commit()


    # ~~ FECHAR CONEXÃO COM O BANCO ~~
    def close(self):

        self.connection.close()