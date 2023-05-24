F = float(input())
C = (F - 32)*5/9
K = C + 273.15

if C.is_integer():
    C = int(C)
if K.is_integer():
    K = int(K)

print('{:g}'.format(C, 3), '{:g}'.format(K, 3))
