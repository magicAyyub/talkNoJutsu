import json
import asyncio
import aiofiles
from src.settings import BASE_DIR
from src.read.base_doc import BaseDoc
from src.talk.sound import Sound


async def main():
    # Create an instance based on file extension
    doc = BaseDoc.generate("docs/cote_3.pdf")
    await doc.read()  

    # Create a Sound object
    sound = Sound()

    # Get voices with their details and save them to a JSON file
    voices_file = BASE_DIR / "out" / "voices.json"
    if not voices_file.exists():
        async with aiofiles.open(voices_file, "w") as f:
            voices = await sound.get_voices()  
            await f.write(json.dumps(voices, indent=4))
    
    # Get the audio of some pages
    NUMBER_OF_PAGES = 5
    START = 2
    for i in range(START, NUMBER_OF_PAGES + 1):
        print(f"Getting audio of page {i}")
        speech = await sound.get_audio(doc.get_page(i))  
        async with aiofiles.open(BASE_DIR / "out" / f"page{i}.mp3", "wb") as f:
            print(f"Saving page audio {i}...")
            await f.write(speech)
            BaseDoc.pretty_print("Done.")

if __name__ == "__main__":
    asyncio.run(main())
