"========================Exceptions============================"
# Исключения (ошибки) - объекты которые прерывают работу кода если были вызваны

SyntaxError # исключение которое выходит когда в коде допущена синтаксическая ошибка

# (  -)\ SyntaxError: unexpected EOF while parsoing
# (когда мы не закрыли скобочку или кавычку)

# a =     - SyntaxError: invalid syntax
# (когда мы что-то сделали не по синтаксу питона)

NameError # исключение которое выходит когда мы образаемся к несуществующей переменной 

#abcdefg   - NameError: name 'abcdefg' is not defined 

IndexError # исключение которое выходит когда мы обращаемся по несуществующему индексу

list_ = [1,2,3,4]
# list_[1000]   - IndexError: list index out of range 
# list_.pop(1000)   -IndexError: pop index out of range 


KeyError # исключение которое выходит когда мы образаемся по несуществующему ключу

dict_ = {"a": 1}
# dict_{'b'}    -KeyError
# dict_{'b'}


ValueError #выходит когда мы пытаемся распаковать какую-то последовательность  где количество переменных и элементов в последовательности не совпадает 
# или когда 
#a,b,c - 'ab'   - ValueError: not enough values to unpack (expected 2, got 2)
a,b = 'ab' # 2 символа могут распаковаться на 2 переменные 
#int('10d')  -ValueError: invalid literal for int() with base 10: '10d'

TypeError # когда мы пытаемсч использовать методы не свойственные какому-то типу данных

#for i in 12345678:  -TypeError: 'int' object is not iterable 
#    print(i)

#5 + "5"    - TypeError: unsupported operand type(s) for +: 'int' and 'str'

#"5" + 5    - TypeError: can only concanate str (int "int") to str

#hash([1,2])     -TypeError: unhashable type: 'list'

#{[1,2,3]: "hello"}     -TypeError: unhashable type: 'list'

#input('hello', 1)   - TypeError: input expected at most 1 argumnet, got 2

# [].append()   - TypeError: append() takes exactly one argument (0 given)

# [].append(1,2)   - TypeError: append() takes exactly one argument (2 given)

IndentationError # когда мы неправильно используем отступы
#   a=4     -IndentationError: unexpected indent
# a=4
#for i in range(1):
#print(i)     -IndentationError: expected an indent block


ZeroDivisionError #выходит при делении на 0
#3 // 0     -ZeroDivisionError 


AttributeError # выходит когда мы обращаемся к несуществуещему аттрибуту или методу объекта

# [].replace('a', '')   -AttributeError: 'list' object has no attribute 'replace'



"===========================Обработка исключений============================"
# чтобы код не прекращал свою работу при некорректных данных

try:
    код который может вызвать ошибку
except Ошибка которая может возникнуть:
    код, который сработает, если в try ошибка вышла
finally:
    код который сработает в любом случае


try:
    num = int(input())
except ValueError:
    print('введите число')
else:
    print('введеное число', num)

# если в input придет число - выйдет то, что мы написали в else 
# если в input придет не число - выйдет то, что мы написали в except

try:
    num = int(input('abcdefg'))
    print('введенное число', num)
except ValueError:
    print('введите число')
else:
    print('введеное число', num)

# raise - вызвать ошибку 

try:
    raise NameError
except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')
except KeyError:
    print('KeyError')


try:
    raise ValueError
except (ValueError, TypeError, KeyError):
    print('была обработана одна ошибка из (ValueError), TypeError, KeyError, SyntaxError')

try:
    raise SyntaxError
except:     #отлавливает все ошибки
    print("была обработана ошибка")

