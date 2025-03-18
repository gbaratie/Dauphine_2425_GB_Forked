class UploadedFile:
    def __init__(self, filename: str, content: bytes):
        self.filename = filename
        self.content = content