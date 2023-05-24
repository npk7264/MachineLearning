# k + 1 là số ga tàu, đánh số từ 0 đến k
# t là số phút ngồi trên tàu 
k, t = map(int, input().split())

def getStation(k, t):
    # x là số lần tàu đi từ ga 0 đến ga k (hoặc ngược lại)
    if t % k != 0:
        x = int(t/k)+1
    else:
        x = int(t/k)
    
    # nếu số chuyến tàu chẵn -> lượt cuối là lượt về
    if x % 2 == 0:
        return k*x-t
    # nếu số chuyến tàu lẻ -> lượt cuối là lượt đi
    else:
        return t-(x-1)*k

print(getStation(k, t))
