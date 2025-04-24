class WebsocketService:
    def __init__(self, active_connections):
        self.active_connections = active_connections

    async def send_update_to_clients(self, data):
        for connection in self.active_connections:
            await connection.send_json(data)
