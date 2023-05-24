import heapq

def shortest_path(m, n, start_x, start_y, end_x, end_y, matrix):
    # Khởi tạo mảng khoảng cách với giá trị vô cực, trừ điểm bắt đầu có giá trị là 0
    distance = [[float('inf') for j in range(n)] for i in range(m)]
    distance[start_x][start_y] = 0
    
    # Khởi tạo hàng đợi ưu tiên từ đầu vào
    pq = [(0, start_x, start_y)]
    
    # Duyệt hàng đợi ưu tiên
    while pq:
        # Lấy đỉnh có khoảng cách ngắn nhất từ đỉnh bắt đầu
        dist, x, y = heapq.heappop(pq)
        
        # Nếu đỉnh đang xét là đỉnh đích, trả về khoảng cách ngắn nhất từ đỉnh bắt đầu đến đỉnh đích
        if x == end_x and y == end_y:
            return dist
        
        # Duyệt các đỉnh kề của đỉnh hiện tại và cập nhật khoảng cách ngắn nhất
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != "1":
                if matrix[nx][ny] == "0": cost = 1
                else: int(matrix[nx][ny])
                if distance[x][y] + cost < distance[nx][ny]:
                    distance[nx][ny] = distance[x][y] + cost
                    heapq.heappush(pq, (distance[nx][ny], nx, ny))
    
    # Nếu không tìm được đường đi, trả về -1
    return -1

# input
m, n, start_x, start_y, end_x, end_y = map(int, input().split())
matrix = []
for i in range(m):
    matrix.append(input().replace(" ",""))
matrix.reverse()

# output
result = shortest_path(m, n, start_x, start_y, end_x, end_y, matrix)
print(result)