import json

class SavePredictIntoDb():
    def __init__(self, repository):
        self.repository = repository

    def save(self, inputData, outputData):
        data = json.loads(inputData.json())

        self.repository.save(
            ratio_to_median_purchase_price=data['ratio_to_median_purchase_price'],
            online_order=data['online_order'],
            distance_from_home=data['distance_from_home'],
            distance_from_last_transaction=data['distance_from_last_transaction'],
            result=outputData['prediction']['value']
        )

        return True
