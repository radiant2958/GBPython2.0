class InvalidIdError(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self) -> str:
        return f'Invalid id: {self.id}. Id should be a 6-digit positive integer between 100000 and 999999.'