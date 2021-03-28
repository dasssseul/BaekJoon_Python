
#기본수학1

#2839_설탕배달
n = int(input())
sugar = 0
while n>=0:
    if n%5 == 0: #n이 5의 배수라면
        sugar += n//5 #n을 5로 나눈 몫을 더해줌
        print(sugar)
        break
    n -= 3 #n이 5의 배수가 아니라면, 5의 배수가 될 때까지 3을 빼줌
    sugar+=1 #봉지의 개수는 하나씩 늘어남
else:
    print(-1)


#기본수학2

#1085_직사각혐에서 탈출
x, y, w, h = map(int, input().split())
if w-x < x:
    rec_x = w-x
else:
    rec_x = x
if h-y < y:
    rec_y = h-y
else:
    rec_y = y
if rec_x < rec_y:
    print(rec_x)
else:
    print(rec_y)


#4153_직각삼각형
pita = list(map(int, input().split()))
while sum(pita) != 0:
    pita = sorted(pita)
    if pita[2]**2 == pita[0]**2 + pita[1]**2:
        print('right')
    else:
        print('wrong')
    pita = list(map(int, input().split()))
    
    
