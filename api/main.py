from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controller.predictController import PredictController
from models.predictModel import PredictJsonModel
from services.databaseSetup import DatabaseSetup

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:5173"] para restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

predict_controller = PredictController()
database_setup = DatabaseSetup(db='database/database.db')

database_setup.setup()

@app.post("/predict")
async def post_predict(data: PredictJsonModel):
    return predict_controller.post(data)

@app.get("/predict")
async def get_predict():
    return predict_controller.get()
