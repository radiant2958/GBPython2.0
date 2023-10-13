class InvalidNameError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f'Invalid name:{self.value}. Name should be a non-empty string.'