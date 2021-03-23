# 10991
n = int(input())
for i in range(n-1,-1,-1):
    print(' '*i+'* '*(n-i))

# 10871
n, x = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] < x :
        print(a[i],end=' ')

# 10872
n = int(input())
facto = 1
for i in range(1, n+1):
    facto *= i
print(facto)

# 1978
n = int(input())
x = list(map(int, input().split()))
final_c = 0
for i in x:
    count = 0
    for j in range(1,1001):
        if i % j == 0:
            count += 1
    if count == 2:
        final_c += 1
print(final_c)

# 2581
m = int(input())
n = int(input())
final = []
for i in range(m, n+1):
    count = 0
    for j in range(1, n+1):
        if i % j == 0:
            count += 1
            if count > 2:
                break
    if count == 2:
         final.append(i)
if len(final) == 0:
    print(-1)
else:
    print(sum(final))
    print(min(final))
