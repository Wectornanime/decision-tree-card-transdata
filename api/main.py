from fastapi import FastAPI

from controller.predictController import PredictController
from models.predictModel import PredictJsonModel
from services.databaseSetup import DatabaseSetup

app = FastAPI()

predict_controller = PredictController()
database_setup = DatabaseSetup(db='database/database.db')

database_setup.setup()

@app.post("/predict")
async def predict(data: PredictJsonModel):
    return predict_controller.post(data)
