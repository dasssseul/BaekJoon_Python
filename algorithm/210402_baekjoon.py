#기본수학2

#1002_터렛

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    #두 점 사이의 거리
    r = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

    R = [r1, r2, r]
    max_r = max(R)

    #두 원이 일치하는 경우
    if (r == 0) and (r1 == r2):
        print(-1)

    #두 원이 외접, 내접하는 경우
    elif (r == (r1+r2)) or ((sum(R)-max_r) == max_r):
        print(1)

    #두 원이 만나지 않는 경우
    elif max_r > (sum(R)-max_r):
        print(0)

    #두 원이 두 점에서 만나는 경우
    else:
        print(2)
