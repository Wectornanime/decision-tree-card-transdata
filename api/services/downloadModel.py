import os
import gdown

class DownloadModel:
    def __init__(self, file_id: str, modelo_path: str):
        self.file_id = file_id
        self.modelo_path = modelo_path

    def download(self):
        if not os.path.exists(self.modelo_path):
            gdown.download(f"https://drive.google.com/uc?id={self.file_id}", self.modelo_path, quiet=False)

