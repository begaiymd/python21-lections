"====================== Работа с файлами ========================"
# open - функция, которая позволяет открыть файл 


"========== Режимы ============"
# r - read (только для чтения)
# w - write (только для записи (сначала все из файла удаляется, а потом записывается))
# a - append (дозапись (все новое добавляется в конец))
# x - создает файл, если он уже существует - ошибка
# rb - чтение в бинарном виде
# wb - запись в бинарном виде
# ab - дозапись в бинарном виде

open("test.txt") #FileNotFoundError

"когда мы не указываем режим - по умолчанию чтение"

open("test.txt", "w") #создает пустой файл 

"когда файла нет - он создает его"
open("test.txt", "a") #создает пустой файл 


"============================ Read =================================="
file = open("test.txt", "w") # открываем файл в режиме чтения 
res = file.read() #считывает весб файл и возвращает строку
print(file.read(5)) # пустая строка потому что каретка находится в самом конце файла
file.seek(0) # каретка переходит в индекс 0 (в начало файла)
print(file.read(5)) # 'hello' (считал 5 символов)
print(file.read(5)) # ' worl' (считал следующие 5 символов)
print (file.tell()) # 10 (показывает текущее положение каретки)
res = file.readlines() # ['d\n', 'Makers Bootcamp\n', 'line1\n', 'line2\n', 'line3\n']
file.seek(0)
print(file.readlines(28))
file.close()


"============================ Write =================================="
file = open("test.txt", "w") # открыл файл, почистил
# res = file.read() io.UnsupportedOperation: not readable
# метод read нельзя использовать при режиме записи и дозаписи 
file.write("hello world") # в файл записали строку hello world 
file.write("Makers Bootcamp") # после этого продолжает писать строку Makers Bootcamp

file.writelines(["line1", "line2", "line3"]) #принимает список со строками и дозаписывает их в файл
file.close() #обязательно закрываем файл


"============================= With ==================================="
# with - конструкция, которая в начале конструкции вызывает метод __enter__, а в конце вызывает __exit__

class Test:
    def __enter__(self):
        print("Начало работы")
        return self
    
    def __exit__(self, *args, **kwargs):
        print("Конец работы")
    
    def hello(self):
        print("Hello world")

with Test() as test:
    test.hello()

# Начало работы
# Hello World
# Конец работы


file1 = open("test.txt", "w")
file1.write("hello")
file1.close()
file2 = open("test.txt", "w")
file2.write("world")

# file1.write("abcdefg") #ValueErorL I/O operation on closed file
# потому что f1 закрыли 



file= open("test.txt", 'w')
file.write("Hello world\nMakers\nBootcamp")
file.seek(0)
file.write("New lines\n")
file.write(res)
file.close()


with open("test.txt") as file:
    print(file.read())
    print(file.closed) #False
print(file.closed) #True
