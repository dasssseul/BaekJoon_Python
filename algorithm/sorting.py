
# 백준 단계별로 풀어보기
# 정렬(sorting)


# 2751번. 수 정렬하기2

import sys
n = int(sys.stdin.readline())

sorting = []
for i in range(n):
    sorting.append(int(sys.stdin.readline()))

sorting.sort()

for i in sorting:
    print(i)


    
# 10989번. 수 정렬하기 3


# 카운팅 정렬 이용_메모리 초과

import sys
n = int(sys.stdin.readline())

sorting = []
for i in range(n):
    sorting.append(int(sys.stdin.readline()))

counting = [0] * max(sorting)

for i in range(len(sorting)):
        counting[sorting[i]-1] += 1

for i in range(len(counting)):
    for j in range(counting[i]):
        print(i+1)


# 배열을 모두 선언하고 출력

import sys
n = int(sys.stdin.readline())

counting = [0]* 10001

for i in range(n):
    number = int(sys.stdin.readline())
    counting[number] += 1

for i in range(len(counting)):
    if counting[i] != 0:
        for j in range(counting[i]):
            print(i)


            
# 2108번. 통계학

# Counter 없이 구현_시간 초과

import sys

n = int(sys.stdin.readline())

number = []
for i in range(n):
    number.append(int(sys.stdin.readline()))

number.sort()

avg = sum(number)/len(number)
median = number[(n+1)//2-1]
difference = max(number) - min(number)

def mode(number):
    cnt = 0
    result = []
    for i in number:
        if number.count(i) > cnt:
            cnt = number.count(i)
    for i in number:
        if number.count(i) == cnt:
            result.append(i)
    if len(result) == 1:
        return result[0]
    else:
        result = result[cnt:]
        return result[0]


print('%.f' % avg)
print(median)
print(mode(number))
print(difference)


# Counter 클래스 사용

from collections import Counter
import sys

n = int(sys.stdin.readline())

number = []
for i in range(n):
    number.append(int(sys.stdin.readline()))

# 평균 구하기
def mean(number):
    return round(sum(number)/len(number))

# 중앙값 구하기
def median(number):
    number.sort()
    med = number[n//2]
    return med

# 최빈값 구하기
def mode(number):
    # 키, 값의 딕셔너리 형태로 반환해주는 Counter
    cnt = Counter(number)
    # 등장한 횟수를 내림차순으로 정렬
    order = cnt.most_common()
    maximum = order[0][1]
    if len(number) > 1:
        if maximum == order[1][1]:
            mod = order[1][0]
        else:
            mod = order[0][0]
    else:
        mod = order[0][0]

    return mod

# 최대 최소 차이 구하기
def diff(number):
    return max(number) - min(number)

print(mean(number))
print(median(number))
print(mode(number))
print(diff(number))



# 1026번. 보물

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0

a.sort()
b.sort(reverse=True)

for i in range(n):
    result += a[i] * b[i]

print(result)


