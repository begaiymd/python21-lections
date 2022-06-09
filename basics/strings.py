"=================Строки==================="
#строки - неизменяемый тип данных, который предназначен для хранения текста (последовательномти символов), заключенного в одинарные или двойные кавычки  
#синтаксис
from tkinter import N


string1 = 'строка с одинарными кавычками'
string2 = "строка с двойными кавычками"
#error = 'неправильная строка"
string3 = "Don't" # внутри двойных кавычек все одинарные - просто символы 
string4 = '"Makers bootcamp"' # внутри одинарных кавычек все двойные - просто смиволы 

string5 = ''' многострочный текст в одинарных кавычках, тут можно ставить любые кавычки '''

"=============Экранизация строк==============="
# экранизация спец-символов
'\n' #перенос на новую строку 
'\t' #табуляция 
'\\' #отображения \ потому что он является инструкцией, которая влияет на наш код
' \' ' #отображение '
" \" " #отображение "
' \r ' #возвращение каретки в начало строки 
' \v ' # перенос на новую строку со смещением вправо на длину предыдущей строки 

'hello\nworld' 
# hello
# world

'hello\tworld'
#hello     world

'чтобы эранировать нужен символ \\'
# чтобы эранировать нужен символ \

'My website is Latracal \rSolution'
# Solutionte is Latracal

'hello \vworld'
#hello
#     world

"=============Форматирование строк============="

title = ' Плов '
price = 1500
format1 = f'Название: {title}, Цена: {price}'
#Название: Плов, Цена: 1300'

format2 = 'Название: %s, Цена: %s'
print (format2 % ("Гуляш", "250"))
print (format2 % ("Самсы", "70"))
# Название: Гуляш, Цена: 250
# Название: Самсы, Цена: 70

print (format2 % ("Гуляш", "250"), format2 % ("Самсы", "70"), sep='\n')

format3 = 'Название: {}, Цена: {}'
print(format3.format('Шакарап', '35'))
# Название: Шакарап, Цена: 35

"===============Методы строк============="
#методы типов данных - функции, к которым мы обращаемся через точку 
dir (str) #посмотреть все методы класса (типа данных)

hello_world = 3 #CamelCase (Python format)
HelloWorld = 3 #SnakeCase (Java format)

'HELLO'.lower() #'hello'
'hello'.upper() #'HELLO'
'Hello'.swapcase() #'hELLO'
'heLLo'.title() #'Hello'
'hello world'.title() #Hello World  
'hello world'.capitalize() #Hello world
'hello world'.center(20) #'    hello world     '
'hello world'.count('l') #3
'hello world'.startswith ('hell') #true
'hello world'.endswith ('d') #true

"=======================Индексы=================="
#индекс - порядковый номер символа в строке 
'h e l l o  w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
string = 'hellow world'
string [0] # 'h'
string [10] # 'd'
string [5] # ''

#срезы - подстрока строки 
string[0:5] #'hello'
string[0:5] #'hello '
string[2:4] #'ll'
string[0:5][2:4] #'ll'

string[:5] #'hello'
string[6:] #'world'
string[0:11:2] #'hlowrd'
string[::3] #'hlwl'
string[::-1] #'dlrow olleh'
string == string  [::-1] #polyndrom

string = 'mom'
string == string  [::-1]
#True

'hello world'.find ('') #5
'hello world'.find ('o') #4
'hello world'.find ('wo') #6
'hello world'.find ('hello') #0

'hello world'.split() #['hello', world]
'hello world'.split('o') #['hell', 'w', 'rld']
'$'.join(['hello', 'world']) #['hello$world']

''.join('hello world'.split()) # 'helloworld'
'o'.join('hello world'.split('0')) # 'hello world'


"===========Доп инфа============"
a=5 
b=5
print (id(a))
print (id(b))

print(hash(a))
print(hash(a))

id(a) == id(b) #true