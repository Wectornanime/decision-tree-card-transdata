import pandas as pd
import json

class TransformDataInDataFrame:
    def __init__(self, data):
        self.data = data

    def transform(self):
        # Transform the data into a DataFrame

        # Assuming self.data is a data to transform
        df = pd.DataFrame([json.loads(self.data.json())])

        return df
