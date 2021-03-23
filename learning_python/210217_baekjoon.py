# 5086
a, b = map(int, input().split())
while a!=0 and b!=0:
    if b%a == 0:
        print('factor')
    elif a%b == 0:
        print('multiple')
    else:
        print('neither')
    a, b = map(int, input().split())

# 5717
a, b = map(int, input().split())
while a!=0 and b!=0:
    print(a+b)
    a, b = map(int, input().split())

# 9610
n = int(input())
x_pos = []
y_pos = []
Q1, Q2, Q3, Q4, AXIS = 0, 0, 0, 0, 0

for i in range(n):
    x, y = map(int, input().split())
    x_pos.append(x)
    y_pos.append(y)
for j in range(n):
    if x_pos[j] > 0 and y_pos[j] > 0:
        Q1 += 1
    elif x_pos[j] < 0 and y_pos[j] > 0:
        Q2 += 1
    elif x_pos[j] < 0 and y_pos[j] < 0:
        Q3 += 1
    elif x_pos[j] > 0 and y_pos[j] < 0:
        Q4 += 1
    else:
        AXIS += 1

print('Q1: %d\nQ2: %d\nQ3: %d\nQ4: %d\nAXIS: %d' % (Q1, Q2, Q3, Q4, AXIS))

# 8958
n = int(input())
for i in range(n):
    score = 0
    final_s = 0
    check = input()
    for j in range(len(check)):
        if check[j] == 'O':
            score += 1
            final_s += score
        elif check[j] == 'X':
            score = 0
            final_s +=0
    print(final_s)

# 9506
n = int(input())
perfect = []
while n != -1:
    for i in range(1, n-1):
        if n % i == 0:
            perfect.append(i)
    if n == sum(perfect):
        print(n,'=',end=' ')
        for j in range(len(perfect)-1):
            print(perfect[j], end=' + ')
        print(perfect[len(perfect)-1])
    else:
        print('%d is NOT perfect.' % n)
    n = int(input())
    perfect = []

# 9506_다솔이 풀이
while True :
    n = int(input())
    if n == -1 :
        break
    factor = []
    for j in range(1, n) :
        if n % j == 0 :
            factor.append(j)
    if sum(factor) == n :
        print(n, '=', end=' ')
        for l in factor[:-1] :
            print(l, end=' + ')
        print(factor[-1], end='\n')
    else :
        print(n, 'is NOT perfect.')
