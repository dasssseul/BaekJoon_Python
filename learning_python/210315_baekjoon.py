# 10809_string활용
import string
alpha = list(string.ascii_lowercase)
word = list(input())
for i in alpha:
    if i in word:
        print(word.index(i),end=' ')
    else:
        print(-1,end=' ')

# 3058
t = int(input())
for i in range(t):
    number = list(map(int, input().split()))
    even = []
    for j in number:
        if j % 2 == 0:
            even.append(j)
    print(sum(even),min(even))

# 5800
k = int(input())
for i in range(k):
    score = list(map(int, input().split()))
    score.remove(score[0])
    score.sort()
    gap = []
    for j in range(len(score)-1):
        gap.append(score[j+1]-score[j])
    print('Class %d\nMax %d, Min %d, Largest gap %d' % (i+1,max(score),min(score),max(gap)))

# 10870
number = [0, 1]
n = int(input())
for i in range(n-1):
    number.append(number[i]+number[i+1])
print(number[n])

# 5576
w = []
k = []
for i in range(10):
    w.append(int(input()))
for i in range(10):
    k.append(int(input()))
w.sort()
k.sort()
print(sum(w[7:]),sum(k[7:]))

# 5576_한줄코딩
w = sorted([int(input())for i in range(10)])[7:]
k = sorted([int(input())for i in range(10)])[7:]
print(sum(w),sum(k))
