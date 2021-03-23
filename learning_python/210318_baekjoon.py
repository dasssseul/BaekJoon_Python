# 11047
n, k = map(int, input().split())
min_n = 0
coin = []
for i in range(n):
    price = int(input())
    if price <= k:
        coin.append(price)
for i in range(len(coin)-1,-1,-1):
    if k != 0:
        min_n += k//coin[i]
        k = k%coin[i]
print(min_n)

# 2743
word = input()
print(len(word))

# 2744_swapcase함수
word = input()
print(word.swapcase())

# 10953
t = int(input())
for i in range(t):
    a, b = map(int, input().split(','))
    print(a+b)

# 2902_런타임에러
a, b, c = map(str, input().split('-'))
print(a[0]+b[0]+c[0])

# 2902
name = list(map(str,input().split('-')))
for i in name:
    print(i[0],end='')
