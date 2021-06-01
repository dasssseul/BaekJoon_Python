
# 백준_그래프 이론

# 1647번. 도시 분할 계획

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

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

edges = []
result = 0

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))


edges.sort()

last = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

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



