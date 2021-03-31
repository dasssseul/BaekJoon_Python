#기본수학1

#2775_부녀회장이 될테야_재도전

t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    apt = []

    # 0층 1호~n호 사람수 리스트 생성
    for j in range(1, n+1):
        apt.append(j)

    # 층 수 만큼 반복
    for number in range(1, k+1):
        #만약 1층 2호라면, 0층의 1호 + 0층의 2호 구해서 새로운 apt[1]로 저장
        for people in range(1,len(apt)):
            apt[people] = apt[people-1]+apt[people]
    print(apt[n-1])


#기본수학2

#9020_골드바흐의 추측_모범답안참고

isPrime = [False, False] + [True]*10002
for i in range(2, 10002):
    if isPrime[i] == True:
        for j in range(i+i, 10002, i):
            isPrime[j] = False

t = int(input())
for i in range(t):
    n = int(input())
    a = n//2
    b = a
    while a>0:
        if isPrime[a] and isPrime[b]:
            print(a,b)
            break
        else:
            a-=1
            b+=1


#3053_택시기하학

import math
r = int(input())
print("%f" % float(r*r*math.pi))
print("%f" % float(r*r*2))


