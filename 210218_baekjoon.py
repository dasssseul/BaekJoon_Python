# 10162_그리디 알고리즘 몰라서 뻘짓
T = int(input())
a_n, b_n, c_n = 0, 0, 0
rest1, rest2 = 0, 0
a, b, c = 300, 60, 10
if T%a == 0:
    a_n = T//a
    print(a_n,b_n,c_n)
elif T%a != 0:
    a_n = T//a
    rest1 = T-(a*a_n)
    if rest1%b == 0:
        b_n = rest1//b
        print(a_n,b_n,c_n)
    elif rest1%b != 0:
        b_n = rest1//b
        rest2 = rest1 -(b*b_n)
        if rest2%c == 0:
            c_n = rest2//c
            print(a_n,b_n,c_n)
        elif rest2%c != 0:
            print(-1)

# 10162_그리디알고리즘
t = int(input())
a = b = c = d = n = 0
a = t // 300
n = t % 300
b = n // 60
n = n % 60
c = n // 10
n = n % 10
if n != 0:
    print(-1)
else:
    print(a,b,c)

# 10103
n = int(input())
score1, score2 = 100, 100
for i in range(n):
    a, b = map(int, input().split())
    if a < b:
        score1 = score1-b
    elif a > b:
        score2 = score2-a
    else:
        score1 = score1
        score2 = score2
print(score1,score2,sep='\n')

# 10214
T = int(input())
for j in range(T):
    y_win, k_win = 0, 0
    for i in range(9):
        y, k = map(int,input().split())
        if y > k:
            y_win += 1
        elif y < k:
            k_win += 1
    if y_win > k_win:
        print("Yonsei")
    elif y_win < k_win:
        print("Korea")
    else:
        print("Draw")

# 11557
T = int(input())
school_drink = {}
for i in range(T):
    n = int(input())
    for j in range(n):
        key, val = map(str, input().split())
        school_drink[key] = int(val)
    for k, v in school_drink.items():
        if v == max(school_drink.values()):
            print(k)

# 10757
a, b = map(int, input().split())
print(a+b)