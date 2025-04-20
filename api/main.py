from fastapi import FastAPI

from controller.predictController import PredictController
from models.predictModel import PredictJsonModel

app = FastAPI()

predict_controller = PredictController()

@app.post("/predict")
async def predict(data: PredictJsonModel):
    return predict_controller.post(data)
