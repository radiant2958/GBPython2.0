# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

class Circle():
    __pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def circle_length(self):
     return 2 * Circle.__pi * self.radius

    
    def square_circle(self):
       return Circle.__pi * self.radius**2
    
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат

class Rectangle():
   
   def __init__(self, lengh, width):
      self.lengh = lengh
      self.width = width

   def perimetr(self):
      return 2*(self.lengh+self.width)
   
   def square(self):
      return self.lengh*self.width
   

# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Person():
   
   def __init__(self, lastname, firstname, age: int, phone, work):
      self.lastname = lastname
      self.firstname = firstname
      self.__age = age
      self.phone = phone
      self.work = work


   def name_full(self):
      return self.lastname, self.firstname
   

   def to_string(self):
      print(f'Фамилия и имя: {self.lastname, self.firstname}, возраст: {self.__age}, телефон: {self.phone}, должность: {self.work}')

   
   def __birthday(self):
      self.__age += 1
   
   def person_age(self):
      return self.__age
   
   def new_phone(self, new_number):
      self.phone = new_number


# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

class Employee(Person):
   
   def __init__(self, lastname, firstname, age: int, phone, work, id_employee):
      super().__init__(lastname, firstname, age, phone, work)
      self.id_employee = id_employee
      self.access_level = self.__calculate_access_level()


   def __calculate_access_level(self):
      total = sum(int(digit) for digit in str(self.id_employee))
      return total%7
      
   def get_access_level(self):
      return self.access_level 
   
   
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.
    

class Animal():

   def __init__(self, name, birthday, vaccinations):
      self.name =  name
      self.birthday = birthday
      self.vaccinations = vaccinations

   def print_animal(self):
      print(f'Имя {self.name}, дата рождения: {self.birthday},вакцины: {self.vaccinations}')

   def special_properties(self):
      pass
     


class Bird(Animal):
   def __init__(self, name, birthday, vaccinations, sounds, flight_altitude):
      super().__init__(name, birthday, vaccinations)
      self.sounds = sounds
      self.flight_altitude = flight_altitude
   
   def print_animal(self):
      super().print_animal()
      print(f'звук: {self.sounds}, высота полета {self.flight_altitude}')

   def special_properties(self):
      print(f'Высота полета {self.flight_altitude}')



class Fish(Animal):
   
   def __init__(self, name, birthday, vaccinations, depth, type_of_water):
      super().__init__(name, birthday, vaccinations)
      self.depth = depth
      self.type_of_water = type_of_water

   def print_animal(self):
      super().print_animal()
      print(f'глубина обитания: {self.depth}, тип воды обитания: {self.type_of_water}')
   
   def special_properties(self):
      print(f'глубина обитания: {self.depth}, тип воды обитания: {self.type_of_water}')


class Beast(Animal):
   
   def __init__(self, name, birthday, vaccinations, sounds, habutation):
      super().__init__(name, birthday, vaccinations)
      self.sounds = sounds
      self.habutation = habutation

   def print_animal(self):
      super().print_animal()
      print(f'звуки: {self.sounds}, среда обитания: {self.habutation}')
   
   def special_properties(self):
      print(f'звуки: {self.sounds}, среда обитания: {self.habutation}')
   
   
  

   




   

      
