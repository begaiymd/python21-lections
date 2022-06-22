"==============Области видимости и пространства имен================"
locals() #показывает все локальные переменные 
globals() #показывает все глобальные переменные

#LEGB - local, enclosed, global, build-in

"Build-in" # - встроенное пространство имен (все встроенные переменные (print, input, sum, max, min, len, abs, int, str etc))

"Global" # - глобальное пространство имен (все переменные внутри файла, которые создали мы)
# чтобы узнать, что находится в глобальном пространстве, можно использовать функцию globals

"Enclosed" # - пространство находящееся между двумя пространствами

"Local" # - какое-то закрытое пространство

def func(b,c):
    # локальное пространство
    a = 5
    print(locals())
    # {'b': 5, 'c': 2, 'a':5}

func(5,2)

def func():
    #enclosed пространство
    a = "func"
    def inner_func():
        #local пространство
        a = "inner func"
        print(locals()) #{'a': 'inner-func'}
    inner_func()
    print(locals()) #{'a': 'func','inner-func': <function func.<locals>.inner_func at 0x7fa171fa8d30>}

func()

# {"func": {"a": "func", "inner_func": {"a": "inner_func"}}}
print(globals["func"]["a"])



count = 0

def add():
    print(count)
    count += 1 #UnboundLocalError: local variable count referenced before assignment

def add():
    global count
    print(count)
    count += 1

add()
add()
add()
print(count)
#1 2 3 3


a = 'global'
def outer_func():
    a = 'enclosed'

    def inner_func():
        a = 'local'
        print(a) #local

    print(a) #enclosed
    inner_func()    
    
print(a) #global
outer_func()

#global enclosed local


def count(i):
    counter = 0

    def add():
        nonlocal counter
        print(counter)
        counter += 1

    for _ in range(i):
        add()

count(10)




