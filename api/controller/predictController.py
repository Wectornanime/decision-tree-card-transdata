import joblib

from models.predictModel import PredictJsonModel
from services.makePrediction import MakePrediction
from services.transformInDataFrame import TransformDataInDataFrame
from services.savePredictIntoDb import SavePredictIntoDb
from services.getStatsFromDb import GetStatsFromDb

from repository.predictionRepository import PredictRepository

class PredictController:
    def get(self):
        prediction_repository = PredictRepository('database/database.db')
        get_stats_from_db = GetStatsFromDb(repository=prediction_repository)

        stats = get_stats_from_db.getStats()
        return stats

    def post(self, data: PredictJsonModel):
        model = joblib.load('modelos/modelo_random_forest.joblib')

        make_prediction = MakePrediction(model)
        data_frame_transform = TransformDataInDataFrame(data)
        prediction_repository = PredictRepository('database/database.db')
        save_predict_into_db = SavePredictIntoDb(prediction_repository)

        predict = make_prediction.predict(data_frame_transform.transform())
        save_predict_into_db.save(inputData=data, outputData=predict)

        return predict
