import os
import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from typing import List

from controller.predictController import PredictController

from models.predictModel import PredictJsonModel

from services.downloadModel import DownloadModel
from services.databaseSetup import DatabaseSetup
from services.websocketService import WebsocketService

from repository.firebaseRepository import FirebaseRepository
from repository.sqliteRepository import SqliteRepository

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://localhost:5173"] para restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lista para armazenar os WebSockets conectados
active_connections: List[WebSocket] = []

websocket_service = WebsocketService(active_connections=active_connections)

firebase_cred_dict = json.loads(os.getenv('FIREBASE_CREDENCIAL_JSON'))
firebase_repository = FirebaseRepository(cred_path=firebase_cred_dict)

sqlite_repository = SqliteRepository(database='database/database.db')

download_model = DownloadModel(file_id=os.getenv('MODEL_FILE_ID'), modelo_path='modelos/modelo.joblib')
database_setup = DatabaseSetup(db='database/database.db')

predict_controller = PredictController(repository=sqlite_repository, websocket_service=websocket_service)

database_setup.setup()
download_model.download()

@app.post("/predict")
async def post_predict(data: PredictJsonModel):
    return await predict_controller.post(data)

@app.get("/predict")
async def get_predict():
    return predict_controller.get()

@app.websocket("/ws/predict")
async def websocket_predict(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)

    try:
        while True:
            data = predict_controller.get()
            await websocket.send_json(data)
            await websocket.receive_text()
    except WebSocketDisconnect:
        active_connections.remove(websocket)

async def send_update_to_clients():
    for connection in active_connections:
        data = predict_controller.get()
        await connection.send_json(data)
