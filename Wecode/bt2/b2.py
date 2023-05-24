import bisect
from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))


def getResult(a, k, x):
    if x <= a[0]:
        return a[:k]
    if x >= a[-1]:
        return a[-k:]

    index = bisect.bisect_left(a, x)
    low, high = index, index + 1

    rs = []
    if x - a[low] <= a[high] - x or a[low] == x:
        rs.append(a[low])
        low -= 1
    else:
        rs.append(a[high])
        high += 1

    for count in range(1, k):
        if low >= 0 and high > len(a)-1:
            rs.append(a[low])
            low -= 1
        elif low < 0 and high < len(a)-1:
            rs.append(a[high])
            high += 1
        else:
            if x - a[low] <= a[high] - x:
                rs.append(a[low])
                low -= 1
            else:
                rs.append(a[high])
                high += 1
        count += 1
    return rs


try:
    while True:
        k, x = map(int, stdin.readline().split())
        result = getResult(arr, k, x)
        print(min(result), max(result))
except:
    exit()
