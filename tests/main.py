import os
from src.settings import BASE_DIR
from src.read.base_doc import BaseDoc
from src.talk.sound import Sound 


def main():
    """Play book content as audio using os page by page, with controle to pause, resume and stop"""
    # Create a BaseDoc object
    doc = BaseDoc.generate("docs/cote_3.pdf")
    # Read the document
    doc.read()
    # Create a Sound object
    sound = Sound()
    sound.generate_audio("test.wav", doc.get_page(2))
    # Play the audio
    os.system("aplay " + str(BASE_DIR / "out" / "test.wav"))

if __name__ == "__main__":
    main()