import PyPDF2
from .base_doc import BaseDoc

class PDF(BaseDoc):
    def __init__(self, path):
        super().__init__(path)
        self.type = "PDF"

    def read(self):
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
