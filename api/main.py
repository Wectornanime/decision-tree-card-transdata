from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import joblib
from pydantic import BaseModel
import pandas as pd
import json

from services.makePrediction import MakePrediction
from services.transformInDataFrame import TransformDataInDataFrame

app = FastAPI()

class PredictJson(BaseModel):
    ratio_to_median_purchase_price: float
    online_order: int
    distance_from_home: float
    distance_from_last_transaction: float


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


@app.post("/predict")
async def predict(data: PredictJson):
    model = joblib.load('modelos/modelo_random_forest.joblib')
    make_prediction = MakePrediction(model)
    data_frame_transform = TransformDataInDataFrame(data)

    predict = make_prediction.predict(data_frame_transform.transform())

    response = {
        "prediction": int(predict[0])
    }

    return response
