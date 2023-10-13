class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self) -> str:
        return f'Invalid age: {self.age}. Age should be a positive integer.'