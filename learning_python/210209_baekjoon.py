# 11
n, m = map(int, input().split())
result = 0
if n == m:
    result = n**2-1
    print(result)
else:
    result = m*n-1
    print(result)

# 12
num = int(input())
a = []
result = 0
for i in range(0,num):
    a.append(list(map(int,input().split())))
for j in range(0, num):
    result = a[j][0]+a[j][1]
    print("Case #"'%d'": "'%d' % (j+1,result))

# 13
num = int(input())
a = []
result = 0
for i in range(0,num):
    a.append(list(map(int,input().split())))
for j in range(0, num):
    result = a[j][0]+a[j][1]
    print("Case #"'%d'": "'%d'" + "'%d'" = "'%d' % (j+1,a[j][0],a[j][1],result))

# 14
import datetime
now = datetime.date.today()
print(now)
