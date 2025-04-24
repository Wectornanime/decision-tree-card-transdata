import joblib

from models.predictModel import PredictJsonModel
from services.makePrediction import MakePrediction
from services.transformInDataFrame import TransformDataInDataFrame
from services.savePredictIntoDb import SavePredictIntoDb
from services.getStatsFromDb import GetStatsFromDb

class PredictController:
    def __init__(self, repository, websocket_service):
        self.repository = repository
        self.websocket_service = websocket_service

    def get(self):
        get_stats_from_db = GetStatsFromDb(repository=self.repository)

        stats = get_stats_from_db.getStats()
        return stats

    async def post(self, data: PredictJsonModel):
        model = joblib.load('modelos/modelo.joblib')

        make_prediction = MakePrediction(model)
        data_frame_transform = TransformDataInDataFrame(data)
        save_predict_into_db = SavePredictIntoDb(repository=self.repository)

        predict = make_prediction.predict(data_frame_transform.transform())
        save_predict_into_db.save(inputData=data, outputData=predict)

        dashboard_data = self.get()
        await self.websocket_service.send_update_to_clients(dashboard_data)

        return predict
