# 10039
final_s = []
result = 0
for i in range(5):
    final_s.append(int(input()))
    for j in range(5):
        if final_s[i] <= 40:
            final_s[i] = 40
for k in range(5):
    result += final_s[k]
print(int(result/5))

# 1934_시도1
t = int(input()) # 테스트 케이스의 개수
T = []
x = []
n = 1 # 최대공약수 구하기 위한 n
for i in range(0,t):
    T.append(list(map(int,input().split())))# 한 세트마다 리스트에 넣기
for j in range(0,t):
    n = 1
    for k in range(1,45000):
        if ((T[j][0]%k) == 0) and ((T[j][1]%k) == 0): # 한 세트별로 최대 공약수 구하기
            if n < k: # 구한 k가 n보다 크면 n을 k로 바꾸기
                n = k
                continue
            else:
                n = 1
    x.append((T[j][0]//n)*(T[j][1]//n)*n) # 최대공약수를 이용한 최소공배수 구하여 X에 넣기
for i in range(t):
    print(x[i],sep="\n")

# 1934_시도2
t = int(input())
T = []
max = 0
x = []
for i in range(0,t):
    T.append(list(map(int,input().split())))
    if T[i][0] > T[i][1]:
        max = T[i][0]
    else:
        max = T[i][1]
        for j in range(max,((T[i][0])*(T[i][1]))+1):
            if j%T[i][0] == 0 and j%T[i][1] == 0:
                x.append(j)
                break
for k in range(t):
    print(x[k],sep="\n")

# 1934_유클리드 호제법 이용
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x%y)
    return x
def lcm(x, y):
    return (x*y)//gcd(x,y)
t = int(input())
T = []
for i in range(0,t):
    T.append(list(map(int,input().split())))
    print(lcm(T[i][0],T[i][1]))

# 2480
a, b, c = map(int, input().split())
if a==b==c:
    print(10000+a*1000)
elif a==b or b==c:
    print(1000+b*100)
elif a==c:
    print(1000+c*100)
else:
    print(max(a,b,c)*100)

# 4101
a, b = map(int, input().split())
while a!=0 and b!=0:
    if a>b:
        print('Yes')
    else:
        print('No')
    a, b = map(int, input().split())

# 10156
k, n, m = map(int, input().split())
if k*n > m:
    print(k*n-m)
else:
    print(0)
