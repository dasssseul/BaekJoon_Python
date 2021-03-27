# 기본수학1

#2869_달팽이는 올라가고싶다_시간초과
import sys
a, b, v = map(int, sys.stdin.readline().split())
length = day = 0
while True:
    day += 1
    length += a
    if length >= v:
        print(day)
        break
    else:
        length -= b

#2869_달팽이는 올라가고싶다_모범답안
import sys
a, b, v = map(int, sys.stdin.readline().split())
high = (v-b) / (a-b) #정상에 도달하면 밤에는 미끄러지지 않기 때문에 분자에 b 빼주기
if float(high) > int(high): #소수점이 생기는 경우는 다음날로 생각
    print(int(high)+1)
else:
    print(int(high))
    
  
#10250_ACM호텔
for i in range(int(input())):
    h, w, n = map(int, input().split())
    if n%h == 0:
        hn = h
        wn = n//h
    else:
        hn = n%h
        wn = n//h + 1
    if len(str(wn)) == 1:
        wn = '0' + str(wn)
    print(str(hn)+str(wn))
