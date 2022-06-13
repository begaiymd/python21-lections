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



