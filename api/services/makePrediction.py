class MakePrediction():
    def __init__(self, model):
        self.model = model

    def predict(self, data):
        # Perform prediction using the model
        prediction = self.model.predict(data)

        return prediction
