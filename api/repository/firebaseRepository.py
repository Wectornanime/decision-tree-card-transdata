import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

class FirebaseRepository():
    def __init__(self, cred_path: str):
        # Inicializa o Firebase se ainda não tiver sido iniciado
        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)

        self.db = firestore.client()
        self.collection = self.db.collection('predictions')

    def save(
            self,
            ratio_to_median_purchase_price: float,
            online_order: int,
            distance_from_home: float,
            distance_from_last_transaction: float,
            result: int
            ):
        doc = {
            "ratio_to_median_purchase_price": ratio_to_median_purchase_price,
            "online_order": online_order,
            "distance_from_home": distance_from_home,
            "distance_from_last_transaction": distance_from_last_transaction,
            "result": result,
            "date": datetime.now()
        }
        self.collection.add(doc)

    def getCountAllRegisters(self):
        docs = self.collection.stream()
        return len(list(docs))

    def getCountOfClass(self):
        docs = self.collection.stream()
        count_dict = {}
        for doc in docs:
            data = doc.to_dict()
            result = data.get("result")
            if result is not None:
                count_dict[result] = count_dict.get(result, 0) + 1
        return list(count_dict.items())

    def getFeaturesMedia(self):
        docs = self.collection.stream()
        count = 0
        total_ratio = 0
        total_home = 0
        total_last_tx = 0

        for doc in docs:
            data = doc.to_dict()
            total_ratio += data.get("ratio_to_median_purchase_price", 0)
            total_home += data.get("distance_from_home", 0)
            total_last_tx += data.get("distance_from_last_transaction", 0)
            count += 1

        if count == 0:
            return (0, 0, 0)

        return (
            total_ratio / count,
            total_home / count,
            total_last_tx / count
        )
