
# 백준 단계별로 풀어보기
# 동적 계획법(dynamic programming)


# 1003번. 피보나치 함수

d0 = [0] * 41
d1 = [0] * 41
d0[0] = 1
d0[1] = 0
d1[0] = 0
d1[1] = 1

for i in range(int(input())):
    n = int(input())
    for j in range(2, n+1):
        d0[j] = d0[j - 1]+d0[j - 2]
        d1[j] = d1[j - 1] + d1[j - 2]
    print(d0[n], d1[n])



# 9461번. 파도반 수열

d = [0]*101
d[0], d[1], d[2] = 1, 1, 1

for i in range(int(input())):
    n = int(input())
    for j in range(3, n+1):
        d[j] = d[j-2] + d[j-3]
    print(d[n-1])



# 1463번. 1로 만들기

d = [0] * 1000001
n = int(input())

for i in range(2,n+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)

print(d[n])



# 11053번. 가장 긴 증가하는 부분 수열(LIS)

a = int(input())
number = list(map(int, input().split()))

dp = [1] * a

for i in range(1, a):
    for j in range(0, i):
        if number[i] > number[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))



# 1932번. 정수 삼각형

n = int(input())
semo = [list(map(int,input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            semo[i][j] += semo[i-1][j]
        elif j == i:
            semo[i][j] += semo[i-1][j-1]
        else:
            semo[i][j] += max(semo[i-1][j-1], semo[i-1][j])

print(max(semo[n-1]))



# 2156번. 포도주 시식

n = int(input())
podo = [0]
for _ in range(n):
    podo.append(int(input()))

dp = [0] * (n+1)
dp[1] = podo[1]

# 포도주가 1개일 경우 dp[2]를 계산할 수 없기 때문에
# 종료 조건 필요
if n == 1:
    print(dp[1])
    exit()

dp[2] = dp[1] + podo[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-2]+podo[i], dp[i-3]+podo[i-1]+podo[i], dp[i-1])

print(max(dp))





