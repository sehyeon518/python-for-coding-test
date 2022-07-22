# 5-11.py
from collections import deque
N, M = map(int, input().split())

graph = []
for n in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 1

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M and graph[next_x][next_y] == 1:
                graph[next_x][next_y] = graph[x][y] + 1
                queue.append((next_x, next_y))
    return graph[N-1][M-1]

print(bfs(0,0))

'''
5 6
101010
111111
000001
111111
111111
'''
