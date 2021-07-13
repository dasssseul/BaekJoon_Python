
# 백준 단계별로 풀어보기
# 구현(implementation)


# 10448번. 유레카 이론

from itertools import combinations_with_replacement

n = int(input())
result = 0
samgak = []

for j in range(1, 45):
    result += j
    samgak.append(result)

for i in range(n):
    k = int(input())
    for j in combinations_with_replacement(samgak,3):
        if sum(j) == k:
            print(1)
            break
    else:
        print(0)


        
# 2161번. 카드1

n = int(input())
card = []
delete = []

for i in range(1,n+1):
    card.append(i)

while len(card) != 1:
    delete.append(card.pop(0))
    card.append(card.pop(0))


for i in delete:
    print(i, end=" ")
print(card[0])



# 1592번. 영식이와 친구들_ㅠㅠ

n, m, l = map(int, input().split())
cnt = [0]*n
cnt[0] = 1
start = 1

while True:
    if max(cnt) == m:
        print(sum(cnt)-1)
        break
    else:
        if cnt[start-1] % 2 == 1:
            start += l
            if start <= n:
                cnt[start - 1] += 1
            else:
                start -= (2*l+1)
                cnt[start - 1] += 1
        else:
            start += (l + 1)
            if start <= n:
                cnt[start - 1] += 1
            else:
                start -= (2*l+1)
                cnt[start - 1] += 1

                
# 1592번. 영식이와 친구들

n, m, l = map(int, input().split())
cnt = [0]*n
i = 0
result = 0

while True:
    cnt[i] += 1
    if cnt[i] == m:
        print(result)
        break
    i = (i+l)%n
    result += 1
    

    
# 1547번. 공

m = int(input())

ball = [0, 1, 0, 0]

for _ in range(m):
    x, y = map(int, input().split())
    ball[x], ball[y] = ball[y], ball[x]

for i in ball:
    if i == 1:
        print(ball.index(i))



# 백준_구현 복습


# 7568번. 덩치

n = int(input())
people = []
cnt = [1] * n

for i in range(n):
    w, h = map(int, input().split())
    people.append((w, h))

for i in range(n):
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt[i] += 1
    print(cnt[i], end =" ") 

    
    
# 1966번. 프린터 큐

for _ in range(int(input())):
    n, m = map(int,input().split())
    priority = list(map(int, input().split()))
    # 인덱스 확인을 위한 result 배열 0으로 초기화
    result = [0] * n
    # 원하는 문서의 결과만 1로 설정
    result[m] = 1
    # 순서를 구하기위한 cnt 초기화
    cnt = 0

    while True:
        # 첫번째 원소의 중요도가 제일 크다면
        if priority[0] == max(priority):
            # 출력 횟수 +1
            cnt += 1
            # 원하는 문서의 위치가 출력된 것이라면 횟수 출력
            if result[0] == 1:
                print(cnt)
                break
            else:
                # 원하는 문서의 위치가 아니라면 첫번째 원소, 위치 제거
                priority.pop(0)
                result.pop(0)
        # 첫번재 원소의 중요도가 제일 큰 것이 아니라면
        else:
            # 해당 원소 제거 및 제일 오른쪽에 붙여주기 
            priority.append(priority.pop(0))
            result.append(result.pop(0))

            

            
# 10813번. 공 바꾸기

n, m = map(int, input().split())

balls = [0] * (n+1)
for i in range(n+1):
    balls[i] = i

for j in range(m):
    a, b = map(int,input().split())
    balls[a], balls[b] = balls[b], balls[a]

for k in range(1, n+1):
    print(balls[k], end=" ")



# 18406번. 럭키 스트레이트

# 점수 입력 받기
n = int(input())
# 입력받은 점수를 문자열로 변환
n = str(n)

score = []
# 문자 하나씩 정수형으로 변환해 score에 삽입
for i in n:
    score.append(int(i))

# 중간 인덱스 값 구해주기
half = int(len(n)/2)

# 슬라이싱을 이용해 왼쪽 절반의 합과 오른쪽 절반의 합 비교
if sum(score[:half]) == sum(score[half:]):
    print("LUCKY")
else:
    print("READY")



# 5597번. 과제 안 내신 분..?

numbers = []
thirty = [i for i in range(1, 31)]

for _ in range(28):
    numbers.append(int(input()))

numbers.sort()

for i in thirty:
    if i not in numbers:
        print(i)


# 3190번. 뱀

# 보드의 크기 n
n = int(input())
# 사과의 개수 k
k = int(input())
# n x n 배열 초기화
board = [[0] * n for _ in range(n)]
# 뱀의 현재 위치
nx, ny = 0, 0
board[nx][ny] = 2
# 사과의 위치 입력받기
for i in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

# 이동 방향 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 초기 direction은 동쪽
direction = 1

# 방향 변환 함수
def turnleft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

def turnright():
    global direction 
    direction += 1
    if direction == 4:
        direction = 0

# 방향 변환 횟수 입력 받기 
l = int(input())
l_info = [0] * 10001

# 방향 정보 입력 받기
for i in range(l):
    x, c = map(str, input().split())
    l_info[int(x)] = c

# 시간 초기화
time = 0

# 뱀의 머리와 꼬리의 좌표 삽입
q = [[0,0]]

while True:
    # 방향 변환 정보에 따른 회전
    if l_info[time] == 'L':
        turnleft()
    elif l_info[time] == 'D':
        turnright()
    # 뱀의 머리 좌표 업데이트 
    nx += dx[direction]
    ny += dy[direction]
    # 시간 증가
    time += 1
    if (0 <= nx < n) and (0 <= ny < n):
        # 사과가 있다면
        if board[nx][ny] == 1:
            # 머리 좌표만 삽입, 이전의 머리는 꼬리가 됨
            q.append([nx, ny])
            # 뱀의 위치 좌표 업데이트
            board[nx][ny] = 2
        # 사과가 없다면
        elif board[nx][ny] == 0:
            # 머리 좌표 삽입
            q.append([nx, ny])
            # 뱀의 위치 업데이트
            board[nx][ny] = 2
            # 맨 왼쪽 꼬리 좌표 삭제
            del_x, del_y = q.pop(0)
            # 뱀이 없으므로 위치 좌표 업데이트
            board[del_x][del_y] = 0
        # 자기자신과 부딪히면 종료
        elif board[nx][ny] == 2:
             break
    # 벽과 부딪히면 종료 
    else:
        break
# 시간 출력
print(time)



    
