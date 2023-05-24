from sys import stdin

v, e, n = map(int, stdin.readline().split())

# Tạo danh sách tên các đỉnh
vertices = stdin.readline().split()

# Mảng trọng số
w_list = {}

for i in range(e):
    u, v, w = stdin.readline().split()
    w_list[u + " " + v] = w

# Xử lý các thao tác
for i in range(n):
    op = stdin.readline().split()
    if op[0] == '1':
        try:
            print(w_list[op[1] + " " + op[2]])
        except:
            print('FALSE')
    elif op[0] == '2':
        neighbors = []
        # in mảng trọng số theo thứ tự đỉnh tương ứng trong mảng vertices
        for v in vertices:
            try:
                neighbors.append(w_list[op[1] + " " + v])
            except:
                pass
        if neighbors:
            print(' '.join(neighbors))
        else:
            print('NONE')
