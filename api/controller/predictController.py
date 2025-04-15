import joblib

from models.predictModel import PredictJsonModel
from services.makePrediction import MakePrediction
from services.transformInDataFrame import TransformDataInDataFrame

class PredictController:
    def post(self, data: PredictJsonModel):
        model = joblib.load('modelos/modelo_random_forest.joblib')

        make_prediction = MakePrediction(model)
        data_frame_transform = TransformDataInDataFrame(data)

        predict = make_prediction.predict(data_frame_transform.transform())
        return predict
