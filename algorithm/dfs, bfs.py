
# 백준
# 1260번. DFS와 BFS

from collections import deque

n, m, v = map(int, input().split())
visited = [0] * (n+1)
node = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    node[x][y] = node[y][x] = 1

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visited[i] == 0 and node[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] == 0 and node[v][i] == 1:
                queue.append(i)
                visited[i] = 1

dfs(v)
print()
visited = [0] * (n+1)
bfs(v)



