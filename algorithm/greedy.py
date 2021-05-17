
# 백준 단계별로 풀어보기
# greedy 알고리즘


# 11399번_ATM

n = int(input())
p = list(map(int, input().split()))
p = sorted(p)
for i in range(1,n):
    p[i] = p[i-1]+p[i]
print(sum(p))


# 13305번_주유소

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





