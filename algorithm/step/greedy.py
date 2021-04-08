
# 단계별로 풀기
# greedy 알고리즘


# 11399번_ATM

n = int(input())
p = list(map(int, input().split()))
p = sorted(p)
for i in range(1,n):
    p[i] = p[i-1]+p[i]
print(sum(p))


# 13305번_주유소

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
result = dist[0]*cost[0]
min_cost = cost[0]

for i in range(1,len(dist)):
    if cost[i] >= min_cost:
        result += min_cost * dist[i]
    else:
        min_cost = cost[i]
        result += min_cost * dist[i]

print(result)



