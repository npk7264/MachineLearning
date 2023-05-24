import math
a = float(input())
b = float(input())
c = float(input())

if a+b > c and b+c > a and c+a > b:
    # tính diện tích
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    if s == int(s):
        s = int(s)
    else:
        s = round(s, 2)
    
    # xác định loại tam giác
    if(a == b and a != c) or (b == c and b != a) or (c == a and a != b):
        print('Tam giac can, dien tich =', s)
    elif a*a == b*b+c*c or b*b == c*c+a*a or c*c == a*a+b*b:
        print('Tam giac vuong, dien tich =', s)
    elif a == b and b == c:
        print('Tam giac deu, dien tich =', s)
    else:
        print('Tam giac thuong, dien tich =', s)
else:
    print('Khong phai tam giac')
