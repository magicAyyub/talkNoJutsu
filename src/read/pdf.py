import time
import json
from pathlib import Path
import PyPDF2
from .base_doc import BaseDoc
from src.settings import BASE_DIR

class PDF(BaseDoc):
    def __init__(self, path):
        super().__init__(path)
        self.type = "PDF"
        self.old_content_path = BASE_DIR / "out" / f"{Path(self.path).stem}.json"

    async def read(self):
        if self.old_content_path.exists() :
            with open(self.old_content_path, "r") as f:
                self.pages = json.load(f)
            return
        BaseDoc.pretty_print("Reading the document...")
        pdf = PyPDF2.PdfReader(self.path)
        self.pages = []
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            self.pages.append(page.extract_text())
        self.text = "\n".join(self.pages)
        self.preprocess()

        # clean with deleting empty pages or page less than 30 words
        self.pages = [page for page in self.pages if len(page.split()) > 30]

        time.sleep(1)
        # Generate json version of the document for future use
        with open(self.old_content_path , "w") as f:
            json.dump(self.pages, f)
        BaseDoc.pretty_print("Reading is done.")
