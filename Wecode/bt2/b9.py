from sys import stdin
import heapq
m, n, start_x, start_y, end_x, end_y = map(int, stdin.readline().strip().split())
land = []

for i in range(m):
    land.append(list(map(int, stdin.readline().strip().split())))
land.reverse() 
move = [(-1, 0), (0, -1), (0, 1), (1, 0)]
if not land or land[end_x][end_y] == 1:
    print(-1)
elif start_x == end_x and start_y == end_y :
    print(0)
else:
    cost = [[float('inf') for i in range(n)] for j in range(m)]
    cost[start_x][start_y] = 0
    path = []
    heapq.heappush(path,[0, start_x, start_y])
    land[start_x][start_y] = 0
    direction = {}
    direction[(start_x,start_y)] = [(0, 0)]
    while path:
        u, x, y = heapq.heappop(path)
        if land[x][y] == 0:
            land[x][y] = 1
            for (dx, dy) in move:
                if 0 <= x + dx < m and 0 <= y + dy < n and land[x + dx][y + dy] == 0:
                    step = cost[x][y]
                    try:
                        t = direction[(x,y)].index((dx, dy))
                    except:
                        step += 1
                    new_x = x + dx
                    new_y = y + dy
                    if step < cost[new_x][new_y]:
                        direction[(new_x, new_y)] = [(dx, dy)]
                        heapq.heappush(path,[step, new_x, new_y])
                        cost[new_x][new_y] = step
                    elif step == cost[new_x][new_y]:
                        direction[(new_x,new_y)].append((dx, dy))
        else:
            continue
    if cost[end_x][end_y] != 32000:
        print(cost[end_x][end_y])
    else:
        print(-1)