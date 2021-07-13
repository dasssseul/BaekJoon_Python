
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



# 백준

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



# 2667번. 단자 번호 붙이기

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 2
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
danji_num = []
cnt = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            danji_num.append(cnt)
            cnt = 0
print(result)
danji_num.sort()
for i in danji_num:
    print(i)




# 16173번. 점프왕 쩰리

from collections import deque

n = int(input())
jelly = []

# 이동할 리스트의 맵 정보 입력받기
for i in range(n):
    jelly.append(list(map(int, input().split())))

# 오른쪽과 아래로 이동할 방향 정의
dx = [1, 0]
dy = [0, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    visited = [[0]*n for i in range(n)]
    queue.append((x, y))
    # queue가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 가장 아래칸에 도달한 경우 True 반환 후 종료
        if jelly[x][y] == -1:
            return True
        # 오른쪽과 아래 방향으로의 위치 확인
        for i in range(2):
            nx = x + dx[i]*jelly[x][y]
            ny = y + dy[i]*jelly[x][y]
            # 맵을 벗어나지 않고, 방문한 적이 없을 경우 
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
    return False



if bfs(0,0):
    print('HaruHaru')
else:
    print('Hing')





# 16174번. 점프왕 쩰리(Large)

from collections import deque

n = int(input())
jelly = []
for i in range(n):
    jelly.append(list(map(int, input().split())))

dx = [1, 0]
dy = [0, 1]

def bfs(x, y):
    queue = deque()
    visited = [[0]*n for i in range(n)]
    visited[x][y] = 1
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if jelly[x][y] == -1:
            return True
        for i in range(2):
            nx = x + dx[i]*jelly[x][y]
            ny = y + dy[i]*jelly[x][y]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
    return False

if bfs(0,0):
    print('HaruHaru')
else:
    print('Hing')



# 2178번. 미로 탐색

from collections import deque

# 정수 n, m 입력 받기
n, m = map(int, input().split())

# 미로 입력 받기
array = []
for i in range(n):
    x = list(map(int, list(input())))
    array.append(x)


# 현재 위치를 q에 저장
q = deque()
q.append((0,0))

# 방문 처리를 위한 array
visited = [[False] * m for i in range(n)]
visited[0][0] = True

# 방향 설정(북, 동, 남, 서)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 칸 수를 세기 위한 배열 초기화
dist = [[0]*m for i in range(n)]
# 출발지 칸 수 = 1
dist[0][0] = 1

while q:
    # q에서 왼쪽부터 꺼내서 x, y
    x, y = q.popleft()
    # 네 방향 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # nx, ny가 미로 안에 있고
        if (0 <= nx < n) and (0 <= ny < m):
            # 방문한 적이 없고, 이동 가능 칸 1이라면
            if (visited[nx][ny] == False) and (array[nx][ny] == 1):
                # 방문 처리
                visited[nx][ny] = True
                # 칸 수 업데이트
                dist[nx][ny] = dist[x][y] + 1
                # q에 위치 삽입
                q.append((nx, ny))
# 오른쪽 맨 아래 칸의 칸 수 출력
print(dist[n-1][m-1])






    
