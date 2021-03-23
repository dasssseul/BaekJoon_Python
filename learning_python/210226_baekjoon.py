# 1408_내일 다시 풀께용
h1, m1, s1 = map(int,input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
now = h1*3600 + m1*60 + s1
start = h2*3600 + m2*60 + s2
rest = start - now
if rest < 0 :
    rest = rest + 24*3600
rest_h = rest//3600
rest_m = (rest%3600)//60
rest_s = (rest%3600)%60
print("%02d:%02d:%02d" % (rest_h,rest_m,rest_s))

# 2741
n = int(input())
for i in range(1,n+1):
    print(i)

# 2742
n = int(input())
for i in range(n,0,-1):
    print(i)

# 2739
n = int(input())
for i in range(1,10):
    print(n,'*',i,'=',n*i)

# 2438
n = int(input())
for i in range(1,n+1):
    print('*'* i)

# 2439
n = int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'*'* i)

# 2440
n = int(input())
for i in range(n,0,-1):
    print('*'* i)

# 2441
n = int(input())
for i in range(n,0,-1):
    print(' '*(n-i)+'*'* i)
