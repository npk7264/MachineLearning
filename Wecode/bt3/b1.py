from sys import stdin
from collections import defaultdict

# số đỉnh, số cạnh
v, e = map(int, stdin.readline().split())
# danh sách đỉnh
v_list = stdin.readline().split()

# danh sách cạnh
graph = defaultdict(list)
for _ in range(e):
    u, i = stdin.readline().split()
    graph[u].append(i)
    graph[i].append(u)

color = {}
for node in v_list:
    color_code = 0
    used_colors = set()
    for neighbor in graph[node]:
        if neighbor in color:
            used_colors.add(color[neighbor])
    while color_code in used_colors:
        color_code += 1
    color[node] = color_code
    print(color_code, end=" ")
