import sqlite3
from datetime import datetime

class SqliteRepository():
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def save(
            self,
            ratio_to_median_purchase_price: float,
            online_order: int,
            distance_from_home: float,
            distance_from_last_transaction: float,
            result: int
            ):
        self.cursor.execute('''
                        INSERT INTO predictions (
                            ratio_to_median_purchase_price,
                            online_order,
                            distance_from_home,
                            distance_from_last_transaction,
                            result,
                            date
                        ) VALUES (?, ?, ?, ?, ?, ?)
                        ''', (ratio_to_median_purchase_price, online_order, distance_from_home, distance_from_last_transaction, result, datetime.now().isoformat())
                        )
        self.conn.commit()

    def getCountAllRegisters(self):
        self.cursor.execute("SELECT COUNT(*) FROM predictions")

        return self.cursor.fetchone()[0]

    def getCountOfClass(self):
        self.cursor.execute("SELECT result, COUNT(*) FROM predictions GROUP BY result")

        return self.cursor.fetchall()

    def getFeaturesMedia(self):
        self.cursor.execute("""
                            SELECT
                                AVG(ratio_to_median_purchase_price),
                                AVG(distance_from_home),
                                AVG(distance_from_last_transaction)
                            FROM predictions
                            """)

        return self.cursor.fetchone()
