"Класс — в объектно-ориентированном программировании, представляет собой шаблон для создания объектов, обеспечивающий начальные значения состояний: инициализация полей-переменных и реализация поведения функций или методов."


"Объе́кт в программировании — некоторая сущность в цифровом пространстве, обладающая определённым состоянием и поведением, имеющая определённые свойства (атрибуты) и операции над ними (методы"

"Ме́тод в объектно-ориентированном программировании — это функция или процедура, принадлежащая какому-то классу или объекту."

class Dog:
    def voice(self):
        print("gaf gaf")

class Cat:
    def voice(self):
        print('myau')


class Person:
    a = 5 #аттрибут класса
    def __init__(self, name, last_name): #аттрибут объекта
        self.name = name
        self.last_name = last_name

person = Person('Begaiym', 'Daniiarova')
print(person.name)


person = Person()
person.name = 'Begaiym'
print(person.name)


class Person:
    a = 5
    def __init__(self, name):
        self.name = name

person1 = Person('Argen')
person2 = Person('Bekzat')
Person.a = 10
print(person1.a, person2.a)



"Inheritance"
class Human:
    a = 5
    def __init__(self, other_name):
        self.other_name = other_name

class Programmer(Human):
    def __init__(self, age, other_name):
        super().__init__(other_name)
        super().a
        self.age = age

programmer = Programmer(17, 'Begaiym')


# git clone file_name


def func():
    for i in range(10):
        yield i

a = func()
print(next(a))





class A:
    @classmethod #Декоратор — это функция, которая позволяет обернуть другую функцию для расширения её функциональности без непосредственного изменения её кода.
    def create_obj(cls):
        print(cls)
        print('work')


        