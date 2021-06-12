
# 백준 단계별로 풀어보기
# greedy 알고리즘


# 11399번. ATM

n = int(input())
p = list(map(int, input().split()))
p = sorted(p)
for i in range(1,n):
    p[i] = p[i-1]+p[i]
print(sum(p))


# 13305번. 주유소

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
result = dist[0]*cost[0]
min_cost = cost[0]

for i in range(1,len(dist)):
    if cost[i] >= min_cost:
        result += min_cost * dist[i]
    else:
        min_cost = cost[i]
        result += min_cost * dist[i]

print(result)




# 백준_그리디 알고리즘 복습

# 1541번. 잃어버린 괄호

# 아이디어 : 첫번재 마이너스가 나오기 전 값들은 더해주고 그 뒤에 값들은 모두 빼준다

plmi = input().split('-')
numbers = []

for value in plmi:
    plus_value = 0
    # 플러스로 묶여있는 수들을 분리해 더해준다
    plus = value.split('+')
    for i in plus:
        plus_value += int(i)
    numbers.append(plus_value)

# 마이너스가 나오기 전 첫번재 값
n = numbers[0]

for i in range(1, len(numbers)):
    n -= numbers[i]

print(n)



# 1931번. 회의실 배정

n = int(input())
time = []

# 회의시간 입력 받기
for i in range(n):
    a, b = map(int, input().split())
    time.append((a, b))

# 시작시간을 기준으로 오름차순 정렬
time_start = sorted(time, key = lambda x : x[0])
# 시작시간 기준으로 정렬된 리스트를 종료시간 기준으로 정렬
time_end = sorted(time_start, key = lambda x : x[1])

end = 0
cnt = 0
for i in time_end:
    if i[0] >= end:
        end = i[1]
        cnt += 1

print(cnt)



# 1439번. 문자열 뒤집기

# 문자열 입력받기
s = input()

# 전부 0으로 바꾸는 경우
count0 = 0

# 전부 1로 바꾸는 경우 
count1 = 0

# 첫 번째 원소에 대해서 처리
if s[0] == '0':
    count1 += 1
else:
    count0 += 1

# 두 번째 원소부터 모든 원소를 확인하면서
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        # 다음 수가 0일 경우 1로 바꿔줘야하기 때문에 count1 + 1
        if s[i+1] == '0':
            count1 += 1
        # 다음 수가 1일 경우 0으로 바꿔줘야하기 때문에 count0 + 1
        else:
            count0 += 1

# 뒤집는 횟수의 최솟값 출력
print(min(count0, count1))



# 2437번. 저울

# 추의 개수 입력 받기
n = int(input())

# 추의 단위 입력 받기
coin = list(map(int, input().split()))

# 추의 단위 오름차순 정렬
coin.sort()

# 더해서 만들 수 있는지 확인할 타켓 설정
target = 1


for i in coin:
    # 만들 수 없는 무게를 찾았을 때 반복 종료
    if target < i:
        break
    target += i

print(target)


