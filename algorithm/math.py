
# 백준

# 11050번. 이항계수1

from itertools import combinations

n, k = map(int, input().split())
n_list = []

for i in range(n):
    n_list.append(i)

result = combinations(n_list, k)
print(len(list(result)))


