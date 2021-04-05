
#greedy 알고리즘

#11399번_ATM

n = int(input())
p = list(map(int, input().split()))
p = sorted(p)
for i in range(1,n):
    p[i] = p[i-1]+p[i]
print(sum(p))



