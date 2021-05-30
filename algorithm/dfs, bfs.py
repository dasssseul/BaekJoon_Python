
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




# 4963번. 섬의 개수

def island_dfs(x, y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 2
        island_dfs(x-1, y)
        island_dfs(x-1, y-1)
        island_dfs(x, y-1)
        island_dfs(x+1, y-1)
        island_dfs(x+1, y)
        island_dfs(x+1, y+1)
        island_dfs(x, y+1)
        island_dfs(x-1, y+1)
        return True
    return False


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    result = 0
    for i in range(h):
        graph.append(list(map(int,input().split())))
    for j in range(h):
        for k in range(w):
            if island_dfs(j, k) == True:
                result += 1
    print(result)


    


