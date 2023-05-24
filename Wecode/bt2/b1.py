n = int(input())
arr = list(map(int, input().split()))
k, x = map(int, input().split())

distance_list = []  # lưu cặp khoảng cách, giá trị
for i, item in enumerate(arr):
    distance_list.append((abs(x - item), item))

distance_list.sort()  # sắp xếp theo khoảng cách -> giá trị (nếu khoảng cách bằng nhau)
print(distance_list)
result = [distance_list[i][1] for i in range(k)]  # lọc lấy giá trị
result.sort()

print(*result)
