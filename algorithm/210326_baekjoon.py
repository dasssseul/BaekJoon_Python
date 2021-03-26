# 문자열


# 1316_그룹단어체커

n = int(input())
group = 0

for i in range(n):
    word = input()
    error = 0
    for j in range(len(word)-1):
        if word[j] != word[j+1]: #연달아있는 두 글자가 같지 않다면
            new_word = word[j+1:] #현재 글자 이후부터 새로운 단어 생성
            if word[j] in new_word: #현재 글자가 새로운 단어에도 있다면
                error += 1 #에러 1증가
    if error == 0:
        group += 1
print(group)


# 기본수학1


# 1712_손익분기점_시간초과주의..
a, b, c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print(int(a/(c-b)+1))


# 2292_벌집
n = int(input())
bee = 1
plus = 6
count = 1

if n == 1:
    print(count)
else:
    while True:
        bee += plus
        count += 1
        if n <= bee:
            print(count)
            break
        plus+=6


# 1193_분수찾기_내코드
n = int(input())
result = 0 #지금까지 총 분수의 개수
plus = 1 #지그재그가 변할 때마다 변하는 분수의 개수
cnt = 1 #분자와 분모를 더해서 나오는 수
fraction= []

while True:
    result = result + plus
    cnt += 1
    if result < n:
        plus += 1
    else:
        if plus % 2 == 1:
            for i in range(1, cnt):
                fraction.append(str(i) + '/' + str(cnt - i))
            print(fraction[result - n])
            print(fraction)
        else:
            for i in range(cnt - 1, 0, -1):
                fraction.append(str(i) + '/' + str(cnt - i))
            print(fraction[result - n])
            print(fraction)
        break

# 1193_분수찾기_모범답안
n = int(input())
count = 0

while n > 0:
    n -= 1
    i += 1

n = i+n-1
res = str(n)+'/'+str(i-n)
if i%2 == 0:
    res = str(i-n)+'/'+str(n)

print(res)

