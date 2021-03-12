# 10818
import sys
n = int(sys.stdin.readline())
number = list(map(int, input().split()))
print(min(number),max(number))

# 5054
t = int(input())
for i in range(t):
    result = 0
    n = int(input())
    store = list(map(int, input().split()))
    result = (max(store) - min(store))*2
    print(result)

# 2822
score = []
for i in range(8):
    n = int(input())
    score.append(n)
s_score = sorted(score)[3::]
print(sum(s_score))
for j in range(8):
    if score[j] in s_score:
        print((j+1),end=' ')

# 2750
n = int(input())
result = []
for i in range(n):
    number = int(input())
    result.append(number)
result = sorted(result)
for j in result:
    print(j)

# 2752
three = sorted(list(map(int, input().split())))
for i in three:
    print(i,end=' ')
