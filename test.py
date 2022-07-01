# try:
#     raise ValueError
# except (ValueError, TypeError, KeyError):
#     print('была обработана одна ошибка из (ValueError), TypeError, KeyError, SyntaxError')

# try:
#     raise SyntaxError
# except:     #отлавливает все ошибки
#     print("была обработана ошибка")




# """
# 3) Напишите функцию, которая принимает список чисел и возвращает их произведение.
# """

# list_ = [1,2,3,4]
# def summa(list_):
#     sum1 = 1
#     for i in list_:
#         sum1 = sum1 * i
#     return sum1
# print(summa(list_))


# list1 = functools.reduce(map(lambda a,b : a*b, list_))



# from pprint import pprint
# file1 = open('hangman.py', 'r')
# data = file1.readlines()
# pprint(data)
