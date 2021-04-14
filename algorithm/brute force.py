
# 백준 단계별로 풀어보기
# 브루트 포스(brute force)_완전 탐색

# 2798번. 블랙잭

n, m = map(int, input().split())
number = list(map(int, input().split()))

result = 0

for i in range(len(number)):
    for j in range(i+1, len(number)):
        for k in range(j+1, len(number)):
            blackjack = number[i]+number[j]+number[k]
            if result < blackjack <= m :
                    result = blackjack
print(result)

# 2798번. 블랙잭_조합 이용시

from itertools import combinations

n, m = map(int, input().split())
number = list(map(int, input().split()))

result = 0

for i in combinations(number, 3):
    blackjack = sum(i)
    if result < blackjack <= m:
        result = blackjack

print(result)


# 2231번. 분해합

n = int(input())

for i in range(1, n+1):
    result = i
    for j in str(i):
        result += int(j)
    if result == n:
        print(int(i))
        break
    if i == n:
        print(0)


