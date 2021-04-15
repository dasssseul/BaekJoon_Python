
# 백준 단계별로 풀어보기
# 구현(implementation)


# 10448번. 유레카 이론

from itertools import combinations_with_replacement

n = int(input())
result = 0
samgak = []

for j in range(1, 45):
    result += j
    samgak.append(result)

for i in range(n):
    k = int(input())
    for j in combinations_with_replacement(samgak,3):
        if sum(j) == k:
            print(1)
            break
    else:
        print(0)


# 2161번. 카드1

n = int(input())
card = []
delete = []

for i in range(1,n+1):
    card.append(i)

while len(card) != 1:
    delete.append(card.pop(0))
    card.append(card.pop(0))


for i in delete:
    print(i, end=" ")
print(card[0])


# 1592번. 영식이와 친구들_ㅠㅠ

n, m, l = map(int, input().split())
cnt = [0]*n
cnt[0] = 1
start = 1

while True:
    if max(cnt) == m:
        print(sum(cnt)-1)
        break
    else:
        if cnt[start-1] % 2 == 1:
            start += l
            if start <= n:
                cnt[start - 1] += 1
            else:
                start -= (2*l+1)
                cnt[start - 1] += 1
        else:
            start += (l + 1)
            if start <= n:
                cnt[start - 1] += 1
            else:
                start -= (2*l+1)
                cnt[start - 1] += 1

# 1592번. 영식이와 친구들_쉽게!

n, m, l = map(int, input().split())
cnt = [0]*n
i = 0
result = 0

while True:
    cnt[i] += 1
    if cnt[i] == m:
        print(result)
        break
    i = (i+l)%n
    result += 1