import os
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from controller.predictController import PredictController
from models.predictModel import PredictJsonModel
from services.downloadModel import DownloadModel
from services.databaseSetup import DatabaseSetup

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:5173"] para restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

download_model = DownloadModel(file_id=os.getenv('MODEL_FILE_ID'), modelo_path='modelos/modelo.joblib')
predict_controller = PredictController()
database_setup = DatabaseSetup(db='database/database.db')

database_setup.setup()
# download_model.download()

@app.post("/predict")
async def post_predict(data: PredictJsonModel):
    return predict_controller.post(data)

@app.get("/predict")
async def get_predict():
    return predict_controller.get()

@app.websocket("/ws/predict")
async def websocket_predict(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = predict_controller.get()
        print(f"Mensagem recebida do front: {data}")
        await websocket.send_text(f"Recebido: {data}")

