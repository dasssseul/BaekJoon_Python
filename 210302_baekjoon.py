# 2010
import sys
n = int(sys.stdin.readline())
sum = 1
for i in range(n):
    p = int(sys.stdin.readline())
    sum += p
print(sum-n)

# 5522
score = []
for i in range(5):
    s = int(input())
    score.append(s)
print(sum(score))

# 10178
t = int(input())
for i in range(t):
    c, v = map(int, input().split())
    print("You get %d piece(s) and your dad gets %d piece(s)." % (c//v,c%v))

# 9295
t = int(input())
for i in range(1,t+1):
    n1, n2 = map(int, input().split())
    print("Case %d: %d" % (i,n1+n2))

# 10569
t = int(input())
for i in range(t):
    v, e = map(int, input().split())
    print(2-v+e)

# 2921
n = int(input())
final_sum = 0
for i in range(n+1):
    sum = 0
    for j in range(i,n+1):
        set = i+j
        sum += set
    final_sum += sum
print(final_sum)

# 10995
n = int(input())
for i in range(n):
    if i%2 == 0:
        print(' '*0+'* '*n)
    else:
        print(' '*1+'* '*n)