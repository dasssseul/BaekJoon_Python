# 9085
t = int(input())
for i in range(t):
    n = int(input())
    number = []
    number = map(int, input().split())
    print(sum(number))

# 2490
for i in range(3):
    play = list(map(int, input().split()))
    if play.count(0) == 1:
        print('A')
    elif play.count(0) == 2:
        print('B')
    elif play.count(0) == 3:
        print('C')
    elif play.count(0) == 4:
        print('D')
    else:
        print('E')

# 10797
day = int(input())
number = list(map(int, input().split()))
n = 0
for i in number:
    if i == day:
        n+=1
print(n)

# 2506
n = int(input())
ox = list(map(int, input().split()))
score = ox.count(1)
x = 0
for i in range(n-1):
    if ox[i] == 1:
        x += 1
        if ox[i+1] == 1:
            score += x
        else:
            x = 0
print(score)

# 1546
n = int(input())
score = list(map(int, input().split()))
m = max(score)
final_score = 0
for i in score:
    final_score += (i/m)*100
print('%.2f' % (final_score/n))

# 2455
total = []
result = 0
for i in range(4):
    n, m = map(int, input().split())
    result += m
    result -= n
    total.append(result)
print(max(total))