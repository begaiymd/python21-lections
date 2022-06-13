x = int(input())
y = int(input())

if x % y == 0:
    print('x делится на y')
    print(x // y)
else:
    print('x не делится на y')
    print(x // y)
    print(int(x % y)+3)