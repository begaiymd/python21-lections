"=============And or not================="
# and - и
# or - или
a = 5
b = 6

a == 5 and b == 6 # True (правая сторона True, левая тоже True)
a == 5 and b == 5 # False (правая сторона True, но левая False)
a == 4 and b == 5 # False (обе стороны False)

a == 5 or b == 6 # True (правая сторона True, левая тоже True)
a == 5 or b == 5 # True (правая сторона True, но левая False)
a == 4 or b == 5 # False (обе стороны False)

# если обе части выдают True - будет True
# если обе части выдают False - будет False
# если одна часть True, вторая False:
# 1. если стоит and - выйдет False
# 2. если стоит or - выйдет True

not True # False
not False # True
not a == 5 # False (потому что a == 5)
not a == 4 # True (потому что a == 5)


"================Тернарные операторы==============="
#условия в одну строку 
тело1 if условие else тело2 

a = 5 
res= 'Hello' if a == 5 else 'Bye'
print (res)
#Hello если a == 5
#Bye если a !=5



"===================Словари========================="
#Словарь (dict) - изменяемый, итерируемый, неиндексируемый, неупорядоченный тип данных, в котором значения хранятся в парах (ключ : значение)

dict_ = {"a": "hello", "b":2, "c":3}
print (dict_["a"]) #Hello

a = 5
b = 7.0

print(locals())
print (a)

#ключами в словаре могут являться все неизменяемые типы данных 
#значениями в словаре могут являться любые типы данных 
#ключи должны быть уникальными 

 dict_={
     l: "hello",
     "a":4,
     4.5: {"a":5},
     {"s":5}: 44 #TypeError: unhashable type: 'dict'
}

print(dict_[4.5]) # {"a":5}
print(dict_[4.5]["a"]) #5
print(dict_["a"]) #KeyError: "a"


"===========================Методы словаря=================="
dict_.clear() # чистит словарь 
print(dict_) # {}

dict = dict.fromkeys([1,2,4])
print(dict_) #{1:None, 2:None, 4:None}

dict = dict.fromkeys([1,2,4], "hello")
print(dict_) #{1:"hello", 2:"hello", 4:"hello"}

dict_={"a":2, "a":3, "a":4}
print(dict_) #{"a":4}
dict_["a"] = 5
print(dict_) #{"a":5}

dict_ = {"a":1, "b":2}
dict_["a"] # 1
dict_["a"] # KeyError

dict_.get("a") # 1
dict_.get("c") # None
dict_.get("c",5) # 5
dict_.get("a",5) # 1

dict_.keys() #dict_keys(['a', 'b'])
dict_.values() #dict_values ([1,2])
dict_.items() #dict_items(['a',1), ('b',2)])

dict1 = {1:"a", 2:"b", 3:"c"}
dict2 = {3:"d", 4:"e"}
#метод update добавляет пары из второго словаря в первый

dict1.update(dict2)
print(dict1) # {1:"a", 2:"b, 3:"d", 4:"e"}
print(dict2) #{3:"d", 4:"e"}

#метод pop удаляет пару по ключу и возвращает значение 
popped = dict1.pop(3)
print(dict1) #{1: "a", 2:"b", 4:"e"}
print(popped) #d

#метод popitem удаляет и возвращает последнюю пару
print(dict1.popitem())
