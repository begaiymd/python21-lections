"========================Built-in functions============================="


"lambda" # анонимная функция 
# lambda параметры: что функция возвращает 


add = lambda a, b: a + b
print(add(5,4)) # 9


"map" # функция, которая принимает первым аргументом функцию, вторым итерируемый объект.
#map возвращает генератор, в котором все элементы - результат принимаемой функции, в которую мы передали элемент из последовательности 

map_gen = map (int, ["1", "2", "3", "4"])
print(map_gen) # <map object>
print(list(map_gen))

#[1,2,3,4]

# map (int, ["1", "2", "3", "4"])
# int("1") -> 1
# int("2") -> 2
# int("3") -> 3
# int("4") -> 4
# list(map (int, ["1", "2", "3", "4"]) -> [1,2,3,4]

res = list(map(lambda a: a+1, [1,2,3,4,5]))
print(res) #[2,3,4,5,6]

"========map на цикле for=========="
func = lambda a: a+1
# def func(a):
#   return e+1

res = []

for e in [1,2,3,4,5]:
    res.append(func(e))
    print(res) #[2,3,4,5,6]



"filter" # это функция, которая возвращает генератор, принимает функцию и итерируемый объект. 
#результат будет последовательность из элементов итерируемого объекта, которые прошли фильтр (проверку)

#first example
list_ = ["Эртай", "Оомат", "Арген", "Манас", "Бекзат", "Даниел", "Эркайым"]

def startwith_vowels(name):
    vowels = "УЕЯЫАОЭИЮYOAIE"
    if name[0].upper() in vowels:
        return True
    return False
res = list(filter(lambda name: name.upper().startswith(tuple(vowels)), list_))
print(res) # [ Эртай, Оомат, Арген, Эркайым ]


#second example
list_ = ["Эртай", "Оомат", "Арген", "Манас", "Бекзат", "Даниел", "Эркайым"]

def startwith_vowels(name):
    vowels = "УЕЯЫАОЭИЮYOAIE"
    return name.upper().startswith(tuple(vowels))

res = list(filter(startwith_vowels, list_))
print(res) # [ Эртай, Оомат, Арген, Эркайым ]



"==========fileter на цикле for=========="
def startwith_vowels(name):
    vowels = "УЕЯЫАОЭИЮYOAIE"
    return name.upper().startswith(tuple(vowels))

list_ = ["Эртай", "Оомат", "Арген", "Манас", "Бекзат", "Даниел", "Эркайым"]

res = []

.....





"reduce" # нужно импортировать из библиотеки functools
#эта функция принимает функцию и итерируемый объект и возвращает 1 результат 


from functools import reduce 

list_ = [1,2,3,4,5,6,7,8,9]

def mul(a,b):
    return a*b
    res = reduce (mul, list_)
    print(res)


"==========Reduce на цикле for=========="
# берет два элемента из списка
list_ = [1,2,3,4,5,6,7,8,9]

def mul(a,b):
    return a*b

res = list_[0]

for b in list_[1:]:
    res = mul(res, b)
print(res)


"enumerate" # функция, которая принимает последовательность.
# возвращает генератор в котором каждый элемент - tuple состоящий из числа и элемента из последовательности 
# (enumerate - нумерует элементы по дефолту начиная с нуля)

list_ = ["a", "b", "c", "d"]

for i in enumerate(list_):
    print(i)
# (0, "a")
# (1, "b")
# (2, "c")
# (3, "d")

for index, elem in enumerate(list_):
    print("index - ", index, ":", "elem - ", elem)

#index - 0 : elem - a
#index - 1 : elem - b
#index - 2 : elem - c
#index - 3 : elem - d

for i in enumerate(list_[1:]):
    print(i)

# (10, "b")
# (11, "c")
# (12, "d")

"zip" # соединяет последовательности 
list1 = [1,2,3,4,5,6]
list2 = ["a", "b", "c", "d", "e", "f"]
print(list(zip(list1,list2)))
# [(1,'a'), (2,'b'), (3,'c'), (4,'d'), (5,'e'),(6,'f')]
print(dict(zip(list1,)))
# {1,'a', 2,'b', 3,'c', 4,'d', 5,'e',6,'f'}


list1 = [1,2,3,4,5,6]
list2 = ["a", "b", "c", "d", "e", "f"]
list3 = [1.9,2.7,3,4.5]
print(list(zip(list1, list2, list3)))
# [(1,'a', 1.9), (2,'b', 2.7), (3,'c',3.0), (4,'d',4.5)]