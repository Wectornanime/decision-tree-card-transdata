import sqlite3

class DatabaseSetup():
    def __init__(self, db):
        # Conectar (ou criar) o banco
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def setup(self):
        # Criar tabela se não existir
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ratio_to_median_purchase_price REAL,
            online_order INTEGER,
            distance_from_home REAL,
            distance_from_last_transaction REAL,
            result INTEGER,
            date TEXT
        )
        ''')

        self.conn.commit()
        self.conn.close()
