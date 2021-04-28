
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



