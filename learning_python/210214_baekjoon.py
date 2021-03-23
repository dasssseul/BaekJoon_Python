# 3009
r = []
x = 0
y = 0
# 직사각형 세개의 점 리스트에 넣기
for i in range(3):
    r.append(list(map(int,input().split())))
# x좌표끼리 비교해서 x4좌표 구하기
if r[0][0] == r[1][0]:
    x = r[2][0]
elif r[0][0] == r[2][0]:
    x = r[1][0]
else:
    x = r[0][0]
# y좌표끼리 비교해서 y4좌표 구하기
if r[0][1] == r[1][1]:
    y = r[2][1]
elif r[0][1] == r[2][1]:
    y = r[1][1]
else:
    y = r[0][1]
print(x,y)

# 3009 (다른 풀이)
x_nums = []
y_nums = []
# 세개의 x,y좌표 각각 리스트에 넣기
for i in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)
# x, y좌표 중 개수가 1개인 좌표 뽑아내기
for j in range(3):
    if x_nums.count(x_nums[j]) == 1:
        x4 = x_nums[j]
    if y_nums.count(y_nums[j]) == 1:
        y4 = y_nums[j]
print(x4, y4)

# 2476
n = int(input())
dice = []
price = []
for i in range(n):
    dice.append(list(map(int,input().split())))
    for j in range(1):
        if dice[i][j] == dice[i][j+1] == dice[i][j+2]:
            price.append(10000 + dice[i][j] * 1000)
        elif dice[i][j] == dice[i][j+1] or dice[i][j+1] == dice[i][j+2]:
            price.append(1000 + dice[i][j+1] * 100)
        elif dice[i][j] == dice[i][j+2]:
            price.append(1000 + dice[i][j+2] * 100)
        else:
            price.append(max(dice[i][j],dice[i][j+1],dice[i][j+2]) * 100)
print(max(price))

# 2754 딕셔너리 활용
c_score = input()
score = {'A+':4.3,'A0':4.0,'A-':3.7,'B+':3.3,'B0':3.0,'B-':2.7,
         'C+':2.3,'C0':2.0,'C-':1.7,'D+':1.3,'D0':1.0,'D-':0.7,'F':0.0}
print(score[c_score])

# 2884
H, M = map(int, input().split())
if M >= 45:
    print(H,M-45)
elif H >= 1 and M < 45:
    print(H-1,M+60-45)
elif H == 0 and M < 45:
    print(23+H,60+M-45)

# 7567
dish = list(map(str,input()))
length = 10 # 첫번째 그릇의 길이
# 맨 뒤부터 비교하면 첫번째 그릇은 비교가 필요없음!
for i in range(-1,-(len(dish)),-1):
    if dish[i] == dish[i-1]:
        length += 5
    elif dish[i] != dish[i-1]:
        length += 10
print(length)
