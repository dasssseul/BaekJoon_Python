# 8393
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

#2609_유클리드호제법
n1, n2 = map(int,(input().split()))
def GCD(x,y):
    while y != 0:
        (x, y) = (y, x%y)
    return x
def LCM(x,y):
    return (x * y)//GCD(x,y)
print(GCD(n1,n2),LCM(n1,n2),sep='\n')

# 2748_피보나치수열
n = int(input())
x = [0,1]
for i in range(n-1):
    x.append(x[i]+x[i+1])
print(x[n])

# 5565
sum = int(input())
for i in range(9):
    price = int(input())
    sum -= price
print(sum)

# 10950
T = int(input())
for i in range(T):
    n1, n2 = map(int, input().split())
    print(n1+n2)

# 10952
while True :
    n1, n2 = map(int, input().split())
    if n1 == 0 and n2 == 0:
        break
    else :
        print(n1+n2)

# 10984
T = int(input())
for i in range(T):
    N = int(input())
    GPA = 0
    final_C = 0
    for j in range(N):
        C, G = map(float, input().split())
        C = int(C)
        final_C += C
        GPA += C*G
    print("%d %0.1f" % (final_C,GPA/final_C))

# 10833
n = int(input())
rest = 0
for i in range(n):
    student, apple = map(int, input().split())
    rest += apple % student
print(rest)

# 2442
n = int(input())
for i in range(1,n+1):
    print(' '*(n-i) + '*'*(2*i-1))

# 2443
n = int(input())
for i in range(n,0,-1):
    print(' '*(n-i) + '*'*(2*i-1))

# 2444
n = int(input())
for i in range(1,n+1):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n-1,0,-1):
    print(' '*(n-i) + '*'*(2*i-1))

# 2522
n = int(input())
for i in range(1,2*n):
    print(' '*abs(n-i)+'*'*abs(abs(n-i)-n))

# 2523
n = int(input())
for i in range(1,2*n):
    print('*'*abs(abs(n-i)-n))

# 9325
t = int(input())
for i in range(t):
    s = int(input())
    n = int(input())
    price = 0
    for j in range(n):
        q, p = map(int, input().split())
        price += q*p
    print(s+price)

# 2445
n = int(input())
for i in range(1,2*n):
    print('*'*abs(abs(n-i)-n)+' '*2*abs((n-i))+'*'*abs(abs(n-i)-n))

# 2446
n = int(input())
for i in range(0, n):
    print(' '*i +'*'*((n-i)*2-1))
for j in range(n-2,-1,-1):
    print(' '*j +'*'*((n-j)*2-1))

