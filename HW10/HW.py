#  Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. 
# Задания должны решаться через вызов методов экземпляра.



import json
from typing import Callable


class Animal():

   def __init__(self, name, birthday, vaccinations):
      self.name =  name
      self.birthday = birthday
      self.vaccinations = vaccinations

   def print_animal(self):
      print(f'Имя {self.name}, дата рождения: {self.birthday}, вакцины: {self.vaccinations}')

   def special_properties(self):
      pass
     


class Bird(Animal):
   def __init__(self, name, birthday, vaccinations, sounds, flight_altitude):
      super().__init__(name, birthday, vaccinations)
      self.sounds = sounds
      self.flight_altitude = flight_altitude
   
   def print_animal(self):
      print(f'Тип: {Bird.__name__}')
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
      print(f'Тип: {Fish.__name__}')
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
      print(f'Тип: {Beast.__name__}')
      super().print_animal()
      print(f'звуки: {self.sounds}, среда обитания: {self.habutation}')
   
   def special_properties(self):
      print(f'звуки: {self.sounds}, среда обитания: {self.habutation}')
   


class AnimalFactory():
   
    def __init__(self, animal_type):
        self.animal_type = animal_type
    
   
    def _save_to_file_decorator(method: Callable):
        def wrapper(self, *args, **kwargs):
            animal = method(self, *args, **kwargs)
            data = []
            filename = 'animal.json'

            try:
                with open(filename, 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                pass

            animal_data = {
                'type': self.animal_type,
                'name': animal.name,
                'birthday': animal.birthday,
                'vaccinations': animal.vaccinations
            }
            
            if self.animal_type == 'Bird':
                animal_data['sound'] = animal.sounds  # Тут возможно нужно изменить sound на sounds
                animal_data['flight_altitude'] = animal.flight_altitude

            elif self.animal_type == 'Fish':
                animal_data['depth'] = animal.depth
                animal_data['type_of_water'] = animal.type_of_water

            elif self.animal_type == 'Beast':
                animal_data['sound'] = animal.sounds  # Тут возможно нужно изменить sound на sounds
                animal_data['habutation'] = animal.habutation
        
            data.append(animal_data)

            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                
            return animal

        return wrapper
        
    @_save_to_file_decorator
    def create_animal(self, *args, **kwargs):
        if self.animal_type == 'Bird':
            return Bird(*args,**kwargs)
        elif self.animal_type == 'Fish':
            return Fish(*args, **kwargs)
        elif self.animal_type == 'Beast':
            return Beast(*args, **kwargs)
        else:
            raise ValueError('Not animal type')
        
    def load_from_json(self, filename='animal.json'):
        animals = []
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for animal_data in data:
                    animal_type = animal_data["type"]
                    if animal_type == "Bird":
                        animals.append(Bird(
                            animal_data["name"], 
                            animal_data["birthday"], 
                            animal_data["vaccinations"], 
                            animal_data["sound"], 
                            animal_data["flight_altitude"]
                        ))
                    elif animal_type == "Fish":
                        animals.append(Fish(
                            animal_data["name"], 
                            animal_data["birthday"], 
                            animal_data["vaccinations"], 
                            animal_data["depth"], 
                            animal_data["type_of_water"]
                        ))
                    elif animal_type == "Beast":
                        animals.append(Beast(
                            animal_data["name"], 
                            animal_data["birthday"], 
                            animal_data["vaccinations"], 
                            animal_data["sound"], 
                            animal_data["habutation"]
                        ))
        except FileNotFoundError:
            print(f"File '{filename}' not found!")
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file '{filename}'!")
        return animals

   
factory = AnimalFactory('Bird')

parrot = factory.create_animal( "Ева", '01.01.2022', 'да', "чик-чирик", "5 метров")

factory_1 = AnimalFactory('Fish')
goldfish = factory_1.create_animal("Немо", "05.02.2020", "да", "2 метра", "соленая вода")

factory_2 = AnimalFactory('Beast')
lion = factory_2.create_animal("Симба", "01.01.2019", "да", "рррр", "дикая природа")

animals = factory.load_from_json()
for animal in animals:
    animal.print_animal() 