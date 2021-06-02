
# 백준_그래프 이론

# 1647번. 도시 분할 계획

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력 받기
n, m = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (n+1)

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보 입력 받기
for i in range(m):
    a, b, cost = map(int, input().split())
    # 비용 순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용 순으로 정렬
edges.sort()

# 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선
last = 0

# 간선을 하나씩 확인하면서 
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함 
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

# 최종 비용에서 최대 비용을 뺀 결과 출력
print(result-last)





# 1922번. 네트워크 연결

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

computer = []
result = 0

for i in range(m):
    a, b, cost = map(int, input().split())
    computer.append((cost, a, b))

computer.sort()

for x in computer:
    cost, a, b = x
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


