
import pytest
import Person
import Employee
import InvalidNameError, InvalidAgeError, InvalidIdError

@pytest.fixture
def data():
    person = Person.Person("Петров", "Иван", "Иванович", 30)
    return person

def test_last_name(data):
    assert data.last_name == 'Петров'

def test_empty_last_name(data):
    with pytest.raises(InvalidNameError.InvalidNameError):
        data.last_name = ''

def test_istitle_last_name(data):
    with pytest.raises(InvalidNameError.InvalidNameError):
        data.last_name = 'петров'

def test_type_last_name(data):
    with pytest.raises(InvalidNameError.InvalidNameError):
        data.last_name = '786'


def test_first_name(data):
    assert data.first_name == 'Иван'

def test_empty_first_name(data):
    with pytest.raises(InvalidNameError.InvalidNameError):
        data.first_name = ''

def test_istitle_first_name(data):
    with pytest.raises(InvalidNameError.InvalidNameError):
        data.first_name = 'иван'

def test_type_first_name(data):
    with pytest.raises(InvalidNameError.InvalidNameError):
        data.first_name = '746'

def test_age(data):
    with pytest.raises(InvalidAgeError.InvalidAgeError):
        data.age = -29   

def test_employee_id():
    employee = Employee.Employee("Иванов", "Иван", "Иванович", 30, 123456)
    assert employee.id == 123456

def test_employee_unique_id():
    employee1 = Employee.Employee("Иванов", "Aлександр", "Иванович", 30, 123457)
    with pytest.raises(InvalidIdError.InvalidIdError):
        employee2 = Employee.Employee("Петров", "Петр", "Петрович", 31, 123457)  



if __name__ == '__main__':
    pytest.main(['-v'])