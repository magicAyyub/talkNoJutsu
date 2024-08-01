from .base_doc import BaseDoc
import docx

class Docs(BaseDoc):
    def __init__(self, path):
        super().__init__(path)
        self.type = "Docs"
    
    # private cleaning method
    def _clean(self, text:str) -> str:
        text = text.strip()
        text = text.replace("\t", " ")
        text = text.replace("\n", " ")
        text = text.replace("\r", " ")
        return text


    def read(self):
        BaseDoc.pretty_print("Reading the document...")
        doc = docx.Document(self.path)
        self.pages = []
        for para in doc.paragraphs:
            self.pages.append(para.text)
        self.pages = list(map(self._clean, self.pages))
        self.pages = list(filter(lambda x: x, self.pages))
        self.text = "\n".join(self.pages)
        print(self.pages)
        
        

       



    
