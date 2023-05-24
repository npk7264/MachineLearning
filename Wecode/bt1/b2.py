def fibonacci(x):
    if (x==1):
        return 1
    if(x==2):
     return 1
    return fibonacci(x-1)+fibonacci(x-2)


x = int(input())

if x >= 1 and x <= 30:
    print(fibonacci(x))
else:
    print("So", x, "khong nam trong khoang [1,30].")
