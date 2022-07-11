"==========================Инкапсуляция====================="
# Инкапсуляция - принцип ООП
# 1. сокрытие данных (ограничение доступа к определенным методам и классам)
# 2. сбор всех необходимых для класса методов и аттрибутов в капсулу (класс)

"=============Модификаторы доступа к аттрибутам=============="
# 1. public (публичный)
# 2. protected (защищенный)
# 3. private (приватный)

class A:
    attr1 = "публичный"
    _attr2 = "защищенный"
    __attr3 = "приватный"

A.attr1 # 'публичный'
A._attr2 # 'защищенный'
A.__attr3 # Attribute error
print(A._A__attr3) # 'приватный'

"=====================getters / setters===================="
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age


obj = Person("Anna", 18)
# print(obj__age) # AttributeError
print(obj.get_age())


    @property
    def age(self):
        return self.__age


    @age.setter
    def set_age(self, new_age):
        if new_age < 120 and new_age > 0:
            self.__age = new_age
        else:
            raise Exception("age ca nnot be less than 0 and greater than 120")


obj = Person("Anna", 18)
# print(obj__age) # AttributeError
print(obj.get_age)
obj.age = -5
print(obj.age)

