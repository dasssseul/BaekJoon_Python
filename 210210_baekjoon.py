# 16
h, m = map(int, input().split())
t = int(input())
m1 = m+t
h1 = m1//60
m2 = m1%60
h2 = h+h1
if h2 >= 24:
    h2 = h2 - 24
print(h2,m2)

# 17
h, m, s = map(int, input().split())
s1 = int(input())
h1 = s1//3600
m1 = (s1-h1*3600)//60
s2 = (s1-60*m1-3600*h1)
h2 = h+h1
m2 = m+m1
s3 = s+s2
if s3 >= 60:
    m2 = m2+(s3//60)
    s3 = s3-60
if m2 >= 60:
    h2 = h2+(m2//60)
    m2 = m2-60
if h2 >= 24:
    h2 = h2-24*(h2//24)
print(h2,m2,s3)

# 18
a, b = map(int, input().split())
print(a*(b-1)+1)

# 19
n = int(input())
result = 0
for i in range(0, n):
    mars = list(input().split())
    result = float(mars.pop(0))
    for k in range(len(mars)):
        if mars[k] == '#':
            result -= 7
        elif mars[k] == '%':
            result += 5
        elif mars[k] == '@':
            result *= 3
    print('%.2f' % result)

# 20
t = int(input())
result = str()
for i in range(0,t):
    r,s = input().split()
    r = int(r)
    for j in s:
        result = result + (r*j)
    print(result)
    result = str()