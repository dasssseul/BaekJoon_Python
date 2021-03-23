# 1037
n = int(input())
a = list(map(int, input().split()))
print(max(a)*min(a))

# 5543
b_price = []
d_price = []
for i in range(3):
    b = int(input())
    b_price.append(b)
for j in range(2):
    d = int(input())
    d_price.append(d)
print(min(b_price)+min(d_price)-50)

# 2587
number = []
for i in range(5):
    n = int(input())
    number.append(n)
number = sorted(number)
print(sum(number)//5)
print(number[2])

# 1427
n = list(map(int,input()))
n = reversed(sorted(n))
for i in n:
    print(i, end = '')

# 2309_exit()왜필요할까
h7 = []
for i in range(9):
    h7.append(int(input()))
result = sum(h7)
h7.sort()
for i in range(9):
    for j in range(i+1,9):
        if result - h7[i] - h7[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(h7[k])
            exit()

# 9076
t = int(input())
for i in range(t):
    n = list(map(int, input().split()))
    n.remove(max(n))
    n.remove(min(n))
    if max(n)-min(n) >= 4:
        print('KIN')
    else:
        print(sum(n))

# 2693
t = int(input())
for i in range(t):
    n = list(map(int, input().split()))
    n.sort()
    print(n[len(n)-3])

# 5176
t = int(input())
for i in range(t):
    number = []
    p, m = map(int, input().split())
    for j in range(p):
        n = int(input())
        number.append(n)
    number = set(number)
    print(p-len(number))

# 10773_pop이용
k = int(input())
number = []
for i in range(k):
    n = int(input())
    if n == 0:
        number.pop()
    else:
        number.append(n)
print(sum(number))

# 3040
number = []
for i in range(9):
    n = int(input())
    number.append(n)
result = sum(number)
for i in range(9):
    for j in range(i+1, 9):
        if result - number[i] - number[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(number[k])
            exit()
