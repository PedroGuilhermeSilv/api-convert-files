class InvalidTypeForConvert(Exception):
    def __init__(self, message: str = "Invalid type for convert"):
        self.message = message
        super().__init__(self.message)