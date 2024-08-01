from .base_doc import BaseDoc

class ODT(BaseDoc):
    def __init__(self, path):
        super().__init__(path)
        self.type = "ODT"