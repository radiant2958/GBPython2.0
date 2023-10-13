import Person
import InvalidIdError

class Employee(Person.Person):

    _ids = set()
    def __init__(self, last_name, first_name, patronymic, age, id):
        super().__init__(last_name, first_name, patronymic, age)
        self.id = id
        Employee._ids.add(id)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if value >= 999999 or value <= 100000 or value in Employee._ids:
            raise InvalidIdError.InvalidIdError(value)
        self._id=value
        Employee._ids.add(value)
        
    def get_level(self):
        id_sum = sum(map(int, str(self.id)))
        level = id_sum % 7
        return f'уровень сотрудника {level} '
    
    def __str__(self) -> str:
        return super().__str__() + f', id {self.id}' 
    

