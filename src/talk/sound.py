import base64
import os
import json
import requests
from src.settings import API_BASE_URL, VOICE_ID


class Sound:

    def __init__(self, api_key: str = None) -> None:
        api_key = api_key or os.environ.get("SPEECHIFY_API_KEY")
        if not api_key:
            raise ValueError(
                "API key is required, provide it as an argument or set it as an environment variable.")
        self.api_key = api_key

    async def get_audio(self, text: str) -> None:
        url = f"{API_BASE_URL}/v1/audio/speech"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        body = {
            "input": f"<speak>{text}</speak>",
            "voice_id": VOICE_ID,
            "audio_format": "mp3",
        }

        response = requests.post(url, headers=headers, data=json.dumps(body))

        if not response.ok:
            raise Exception(f"{response.status_code} {response.reason}\n{response.text}")

        response_data = response.json()
        decoded_audio_data = base64.b64decode(response_data['audio_data'])

        return decoded_audio_data

    async def get_voices(self) -> list:
        voices = requests.get(f"{API_BASE_URL}/v1/voices",
                              headers={"Authorization": f"Bearer {self.api_key}"}).json()
        return voices
