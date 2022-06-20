"===================Comprehension===================="
#comprehension - генерация последовательностей в одну строку используя цикл

# 1. действие for элемент in итерируемый объект 
# 2. действие for элемент in итерируемый объект if фильтр 

"======================List comprehension============="

list_ = []
for i in range(1,11):
    list_.append(i)
#list_ = [1,2,3,4,5,6,7,8,9,10]

list_ = list((i for i in range(1,11))) 
#list_ = [1,2,3,4,5,6,7,8,9,10]

list = []
for i in range(1,11):
    list_.append(i*2)
#list_ = [1,4,6,8,10,12,14,16,18,20]

list_ = list((i*2 for i in range(1,11))) 
#list_ = [1,4,6,8,10,12,14,16,18,20]


list_ = [i*2 for i in range(1,11)] 
#list_ = [1,4,6,8,10,12,14,16,18,20]

"Создать списов из четных чисел от 1 до 10"
list = []
for i in range (1,11):
    #if not 0 (четное)
    if not i % 2:
        list_.append(i)

list_ = [i for i in range(1,11) if not i%2]
list_ = [i for i in range(2,11,2)]

# list_ = [2,4,6,8,10]

[print(i) for i in range(10)]
# [None,None,None,None,None,None,None,None,None,None]

list_ = ["hello", for in range(10)]
#["hello","hello","hello","hello","hello","hello","hello","hello","hello","hello","hello"]
 
print([input() for i in range(10)])
# на каждой  итерации запрашивает инпут 


" создать список состоящий из чисел от 1 до 10, но вместо чисел написать 'четное' или 'нечетное' "

list_ = ['нечетное' if i % 2 else 'четное' for i in range(1,11)]
print(list_)
# ['нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное','нечетное', 'четное', 'нечетное', 'четное']

list_ = [(i, 'нечетное' if i % 2 else 'четное') for i in range(1,11)]
print(list_)


list1 = [ 1 , 'hello', 3, 'a', 4, 6, 8, 'hw' ]

" создать список из чисел, находящихся в list, заменив их на 'четное' или 'нечетное' "
list_ = [ 'нечетное' if i % 2 else 'четное' for i in list1 if type(i) == int ]

list_ = [ 'нечетное' if i % 2 else 'четное' for i in list1 if type(i) == int or type(i) == float]

"======================Dictionary comprehension============="
# создать словарь, где ключи - числа от 1 до 10, а значения эти числа ввиде строки 
dict_ = dict( (i, str(i)) for i in range(1,11))
# {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}

"даны 2 списка создайте словарь где ключи - элементы 1 списка а значения - второго"
list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c', 'd', 'e']

dict_ = dict(((list1[index], list2[index]) for index in range(len(list1))))
# {1: 'a', 2: 'b', 3: 'c', 4: 'd, 5: 'e'}

dict_ = {list1[index]: list2[index] for index in range(len(list1))}
# {1: 'a', 2: 'b', 3: 'c', 4: 'd, 5: 'e'}

"создайте копию словаря"
dict1 = {"a": 1, "b":2, 4:"c"}
dict2 = { key: value for key, value in dict1.items()}
#{"a":1, "b":2, "c":4}

"поменяйте ключ и значение местами"
dict1 = {"a": 1, "b":2, 4:"c"}
dict2 = {value : key for key, value in dict1.items()}
#{1: "a", 2: "b", "c":4}

"дан словарь, где значения - список с числами, создайте новый словарь, где значения - сумма тех чисел"
dict1 = {
    "a": [1,2,3,4,5],
    "b": [10,30,2,5],
    "c": [74,28,47],
    "d": [4,6,2,92,9]
}
dict2 = {key: sum(value) for key, value in dict1.items()}
print(dict2)
#{'a': 15, 'b':47, 'c':149, 'd': 113}

"=======================Вложенные comprehensions========================="
"создайте словарь, где коючами будут числа от 1 до 10, а значениями списки от 1 до числа (который ключ)"

dict_ = {i : list(range(1, i+1)) for i in range(1,6)}
print(dict_)
#{1: [1], 2: [1,2], 3: [1,2,3], 4: [1, 2,3,4], 5: [1,2,3,4,5]}

dict_ = {i : [j for j in range(1, i+1)] for i in range(1,6)}
print(dict_)
#{1: [1], 2: [1,2], 3: [1,2,3], 4: [1, 2,3,4], 5: [1,2,3,4,5]}

"создайте список, состоящий из 10 списков, в которых строка 'hello world' повторяется 5 раз"

list_=[
    ['hello world' for i in range(5)]
    for i in range(10)
]
print(list_)
#there will be 10 lists with "hello world"