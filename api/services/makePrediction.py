class MakePrediction():
    def __init__(self, model):
        self.model = model

    def predict(self, data):
        # Perform prediction using the model
        prediction = self.model.predict(data)[0]
        probability = self.model.predict_proba(data)[0][1]

        return {
            "prediction": {
                "value": int(prediction),
                "fraudProbability": int(probability)
            }
        }
