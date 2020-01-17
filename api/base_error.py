class BaseError(Exception):
    def __init__(self, error):
        super().__init__(error)
        self.messages = str(error.orig)