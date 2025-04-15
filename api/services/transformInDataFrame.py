import pandas as pd
import json

class TransformDataInDataFrame:
    def __init__(self, data):
        self.data = data

    def transform(self):
        features = [
            "ratio_to_median_purchase_price",
            "online_order",
            "distance_from_home",
            "distance_from_last_transaction"
        ]

        # Assuming self.data is a data to transform
        df = pd.DataFrame([json.loads(self.data.json())], columns=features)

        return df
