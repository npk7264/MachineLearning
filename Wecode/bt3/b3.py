from sys import stdin

graph = {}

while True:
    line = stdin.readline().split()
    if line[0] == '0':
        break
    elif line[0] == '1':
        vertex = line[1]
        if vertex in graph:
            print('DUP')
        else:
            graph[vertex] = set()
            print('ADD')
    elif line[0] == '2':
        start, end = line[1], line[2]
        flag = 0
        if start not in graph:
            graph[start] = set()
            flag = 1
        if end not in graph:
            graph[end] = set()
            flag = 1
        if end in graph[start]:
            print('DUP2')
        else:
            graph[start].add(end)
            print('ADD2' if flag == 1 else "ADD3")

    elif line[0] == '3':
        u, v = line[1], line[2]
        if u not in graph or v not in graph or v not in graph[u]:
            print('FALSE')
        else: 
            print('TRUE')
    elif line[0] == '4':
        vertex = line[1]
        if vertex in graph:
            print(len(graph[vertex]))
        else:
            print('0')
