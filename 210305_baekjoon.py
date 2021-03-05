# 2501
import sys
n, k = map(int,sys.stdin.readline().split())
d = []
for i in range(1, n+1):
    if n % i == 0:
        d.append(i)
if len(d) < k:
    print(0)
else:
    print(d[k-1])

# 2562
total = []
for i in range(9):
    n = int(input())
    total.append(n)
for j in range(9):
    if total[j] == max(total):
        print(total[j])
        print(j+1)

# 2475
n = list(map(int, input().split()))
final_n = 0
for i in range(len(n)):
    final_n += n[i]*n[i]
print((final_n)%10)

# 2747
n = int(input())
x = [0, 1]
for i in range(n-1):
    x.append(x[i]+x[i+1])
print(x[n])

# 2576
number = []
odd = []
for i in range(7):
    n = int(input())
    number.append(n)
for j in number:
    if j % 2 == 1:
        odd.append(j)
if len(odd) == 0:
    print(-1)
else:
    print(sum(odd))
    print(min(odd))