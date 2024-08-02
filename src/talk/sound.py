import json
from pathlib import Path
from src.settings import *
from .tts_model_processor import TTSModelProcessor
from TTS.api import TTS

class Sound:
    # MODEL_LIST_PATH = BASE_DIR + '/out/structured_models.json'
    model_name = "tts_models/en/ljspeech/tacotron2-DDC"
    
    def __init__(self):
        self.tts = TTS(self.model_name, progress_bar=True, gpu=False)
        self.processor = TTSModelProcessor()

    def generate_tts_list(self):
        self.processor.generate_list()  

    def generate_audio(self, path:str, text:str) -> None:
        output_path = BASE_DIR / "out/" / path
        self.tts.tts_to_file(text=text, file_path=str(output_path)) 


