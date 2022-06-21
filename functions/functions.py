"========================Функции======================"
# функция - именованный блок кода, который может принимать аргументы и возвращать результат

#def #define
def my_sum(a, b):
    return a + b

res = my_sum(5,4)
print(res) #9

"=========================Параметры=============================="
# параметры - локальные переменные внутри функции, значения которым мы задаем при вызове функции
# (переменные которые мы указали внутри скобочек при создании функции (когда) написали (def))
# сначала определяем обязательные ........

"=========================Виды параметров======================="
# 1. обязательные 
# 2. необязательные
# 2.1 по дефолту (со значением по умолчанию)(объявляем переменную со значением через =)
# 2.2 args (множество аргументов)
# 2.3 kwargs



"=========================Аргументы=============================="
# аргументы - значения, которые мы передаем параметрам при вызове функции
# сначала всегда передаются позиционные потом именованные 
"=========================Виды аргументов======================="
# 1. позиционные
# 2. именованные (ключ=значение)

def sum_or_add_10(a, b=10):
    #b - параметр с дефолтом 10
    return a + b

print(sum_or_add_10(2,3)) #5
print(sum_or_add_10(5)) #15
print(sum_or_add_10(2,9)) #11
print(sum_or_add_10(15)) #25

def func(*args, **kwargs):
    print(args, kwargs)
    print("args - ", args)
    print("kwargs - ", kwargs)

# args - tuple, в который нам прихолят все аргументы, которые были переданы через запятую (кроме обязательный и по дефолту)
# kwargs - dict, в который нам приходят все аргументы, которые были переданы ввиде ключ=значение (кроме именованных)

func(1,2,3,4,5,6,7, {'a':5}, a=3, b=5)

def func2(a, b=5, *c, **d):
    print("a -", a)
    print("b -", b)
    print("c -", c)
    print("d -", d)


#func2() -TypeError: func2() missing 1 required positional argument: "a"

func2(10)

# a - 10
# b - 5
# c - ()
# d - {}

func2(10,20)

# a - 10
# b - 20
# c - ()
# d - {}

func2(a=10,b=20)

# a - 10
# b - 20
# c - ()
# d - {}

#func2(10,20,30,40,a=5,b=6)     - TypeError: func2() got multiple values for argument 'a'
#потому что а переменную а позиционно мы передали 10, а именованно 5

func2(10,20,30,40)

# a - 10
# b - 20
# c - (30,40)
# d - {}

func2(10,20,30,40, a=5,b=6)

# ошибка

func2(10,20,30,40, c=5,d=6)
# a - 10
# b - 20
# c - (30,40)
# d - {'c':5, 'd':6}



"=================== * ======================="
# * - знак умножения 
# * - распаковка 

list_ = [1,2,3,4,5]
list2 = [*list_] # распаковываем значения в списке в новый список

dict_ = {'a': 3, 'b': 6}
dict2 = {**dict_} #распаковываем пары в словаре в новый словарь 
print(dict2)

len([1,2,3]) #3

def my_len(obj):
    count = 0
    for i in obj:
        count = count + 1
    return count


print(my_len([1,2,3,4,5])) #5
print(my_len('abcdefgh')) #8


database = {
    "Bekzat": "skala",
    "Ertai": "parol",
    "Oomat": "Kyrgyzstan",
    "Imran": "12345",
    "Zhiide": "return",
    "Manas": "Make",
    "Arafat": "54321",
    "Elzhas": "parol",
    "Gulsana": "312"
}

def login(**data):
    username = data.get("username")
    password = data.get("password")

    if username in database:
        if password == database[username]:
            print("login successful")
        else:
            print("incorrect password")
    else:
        print("Incorrect username")

login(username="Manas", password="Make")


def translate(string):
    eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
    ru = "йцукенгшщзхъфывапролджэячсмитьбю"
    if string[0] in eng:
        dictionary = str.maketrans(eng, ru)
    else:
        dictionary = str.maketrans(eng, ru)
    return string.translate(dictionary)

print(translate(input("Введите слово: ")))
