import json
import os
import joblib

from models.predictModel import PredictJsonModel
from services.makePrediction import MakePrediction
from services.transformInDataFrame import TransformDataInDataFrame
from services.savePredictIntoDb import SavePredictIntoDb
from services.getStatsFromDb import GetStatsFromDb

from repository.predictionRepository import PredictRepository
from repository.firebaseRepository import FirebaseRepository

class PredictController:
    def __init__(self):
        firebase_json = os.getenv('FIREBASE_CREDENCIAL_JSON')
        cred_dict = json.loads(firebase_json)

        self.repository = FirebaseRepository(cred_path=cred_dict)

    def get(self):
        get_stats_from_db = GetStatsFromDb(repository=self.repository)

        stats = get_stats_from_db.getStats()
        return stats

    def post(self, data: PredictJsonModel):
        model = joblib.load('modelos/modelo.joblib')

        make_prediction = MakePrediction(model)
        data_frame_transform = TransformDataInDataFrame(data)
        save_predict_into_db = SavePredictIntoDb(repository=self.repository)

        predict = make_prediction.predict(data_frame_transform.transform())
        save_predict_into_db.save(inputData=data, outputData=predict)

        return predict
