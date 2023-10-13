import InvalidAgeError, InvalidNameError

class Person():
    
    def __init__(self, last_name, first_name, patronymic, age):
            self.last_name = last_name
            self.first_name = first_name
            self.patronymic = patronymic
            self.age = age


    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or value == ' ' or not value.istitle():
            raise InvalidNameError.InvalidNameError(value)
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or value == '' or not value.istitle():
            raise InvalidNameError.InvalidNameError(value)
        self._first_name = value
        
    @property
    def patronymic(self):
        return self._patronymic
    
    @patronymic.setter
    def patronymic(self, value):
        if not isinstance(value, str) or value == ' ' or not value.istitle():
            raise InvalidNameError.InvalidNameError(value)
        self._patronymic = value

    @property
    def age(self):
        return self._age 

    @age.setter
    def age(self,value):
        if not isinstance(value, int) or value <= 0:
            raise InvalidAgeError.InvalidAgeError(value)
        self._age = value


    def birthday(self):
        self.age+=1
       
   
    def get_age(self):
        return self.age
    
    def get_last_name(self):
        return self.last_name
    
    def get_first_name(self):
        return self.first_name
    
    def get_patronymic(self):
        return self.patronymic
    
    
    def __str__(self) -> str:
        return f'Фамилия {self.last_name} имя {self.first_name} отчество {self.patronymic}, возраст {self.age}'
    

