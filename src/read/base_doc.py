import time
import re
import json
from pathlib import Path
from colorama import Fore, Style
from src.settings import BASE_DIR

class BaseDoc:
    def __init__(self, path: str) -> None:
        self.path = path
        self.type = None
        self.text = None   
        self.pages = None

    def __str__(self) -> str:
        return self.text
    
    def __repr__(self) -> str:
        return self.text
           
    async def read(self) -> None:
        # check the json format of the file exists
        print(BASE_DIR / "out" / Path(self.path).name)
        if BASE_DIR / "out" / Path(self.path).name:
            with open(BASE_DIR / "out" / Path(self.path).name, "r") as f:
                self.pages = json.load(f)
            return
        BaseDoc.pretty_print("Reading the document...")
        with open(self.path, "r") as f:
            self.text = f.read()
        self.preprocess()
        time.sleep(1)
        # Generate json version of the document for future use
        with open(BASE_DIR / "out" / f"{Path(self.path).stem}.json" , "w") as f:
            json.dump(self.pages, f)
        BaseDoc.pretty_print("Reading is done.")
        

    def save(self, path: str) -> None:
        with open(path, "w") as f:
            f.write(self.text)
    
    def preprocess(self) -> None:
        for i in range(len(self.pages)):
            print("Preprocessing page " + str(i) + "...")

            # Step 1: Remove patterns like "Page X", "page X", "PAGE X", etc.
            self.pages[i] = re.sub(r'page \d+', '', self.pages[i], flags=re.IGNORECASE)

            # Step 2: Split the page into lines
            lines = self.pages[i].strip().split('\n')

            # Step 3: Remove the last line if it contains urls or references
            if lines[:-1] and (re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', lines[-1]) or re.search(r'\[\d+\]', lines[-1])):
                self.pages[i] = '\n'.join(lines[:-1])   
        BaseDoc.pretty_print("Preprocessing is done.")  

    
    def get_pages(self) -> list:
        return self.pages
    
    def get_page(self, i: int) -> str:
        return self.pages[i]
    
    @staticmethod
    def generate(path: str) -> 'BaseDoc':
        if path.endswith(".pdf"):
            from .pdf import PDF
            return PDF(path)
        elif path.endswith(".odt"):
            from .odt import ODT
            return ODT(path)
        elif path.endswith(".docx"):
            from .docs import Docs
            return Docs(path)
        else:
            raise ValueError("Unsupported file type")
        
    @staticmethod
    def pretty_print(text: str) -> None:
        print(Fore.GREEN + text + Style.RESET_ALL)

    


    
    

    