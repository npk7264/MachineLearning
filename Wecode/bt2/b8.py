import heapq
from sys import stdin

def getShortestPath(m, n, start_x, start_y, end_x, end_y, matrix):
    # Khởi tạo mảng khoảng cách
    distance = [[float('inf') for j in range(n)] for i in range(m)]
    distance[start_x][start_y] = 0
    
    # Khởi tạo hàng đợi ưu tiên từ đầu vào
    pq = [(0, start_x, start_y)]
    
    # Duyệt hàng đợi ưu tiên
    while pq:
        # Lấy đỉnh có khoảng cách ngắn nhất từ đỉnh bắt đầu
        dist, x, y = heapq.heappop(pq)
        
        # Nếu đỉnh đang xét là đỉnh đích, trả về khoảng cách
        if x == end_x and y == end_y:
            return dist
        
        # Duyệt các đỉnh kề của đỉnh hiện tại và cập nhật khoảng cách ngắn nhất
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                # thời gian tính ở điểm hiện tại
                time = int(matrix[x][y])
                if distance[x][y] + time < distance[nx][ny]:
                    distance[nx][ny] = distance[x][y] + time
                    heapq.heappush(pq, (distance[nx][ny], nx, ny))

# input
m, n, start_x, start_y, end_x, end_y = map(int, stdin.readline().split())
matrix = []
for i in range(m):
    matrix.append(stdin.readline().strip().replace(" ",""))
matrix.reverse()

# output
result = getShortestPath(m, n, start_x, start_y, end_x, end_y, matrix)
print(result)