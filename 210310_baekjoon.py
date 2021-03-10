# 2953
sum_cook = []
winner = 0
for i in range(5):
    x = list(map(int, input().split()))
    sum_cook.append(sum(x))
for j in range(5):
    if sum_cook[j] == max(sum_cook):
        winner = j+1
print(winner,max(sum_cook))

# 3052_for문 이용
rest = []
new_rest = []
for i in range(10):
    n = int(input())
    rest.append(n%42)
for j in rest:
    if j not in new_rest:
        new_rest.append(j)
print(len(new_rest))

# 3052_set 이용
rest = []
for i in range(10):
    n = int(input())
    rest.append(n%42)
new_rest = set(rest)
rest = list(new_rest)
print(len(rest))

# 1292
a, b = map(int, input().split())
number = []
for i in range(46):
    for j in range(i):
        number.append(i)
print(sum(number[a-1:b]))

# 3460_첫시도 실패
t = int(input())
for k in range(t):
    n = int(input())
    rest = []
    for i in range((n//4)+1):
        rest.append(n%2)
        n //=2
    for j in range(len(rest)):
        if rest[j] == 1:
            print(j,end=' ')

# 3460_filter 도전
print(list(filter(lambda j:rest[j] == 1, range(len(rest)))), end=' ')

# 3460_bin 이용
t = int(input())
for i in range(t):
    n = bin(int(input()))[2:]
    for j in range(len(n)):
        if n[-j-1] == '1':
            print(j, end=' ')

# 3460_또다른풀이
for _ in range(int(input())):
    n = int(input())
    i = 0
    while n > 0:
        if n%2 == 1:
            print(i, end=' ')
        n = n//2
        i += 1

# 10807
n = int(input())
number = list(map(int, input().split()))
v = int(input())
print(number.count(v))