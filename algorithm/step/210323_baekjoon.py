# 단계별로 풀어보기

# 입출력과 사칙연산

# 10718_we love kriii
print('강한친구 대한육군')
print('강한친구 대한육군')

# 10171_고양이
print('''\\    /\\''')
print(''' )  ( ')''')
print('''(  /  )''')
print(''' \\(__)|''')

# 10172_개
print('''|\\_/|''')
print('''|q p|   /}''')
print('''( 0 )"""\\''')
print('''|"^"`    |''')
print('''||_/=\\\\__|''')


# if문

#1330
a, b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')

#14681
x = int(input())
y = int(input())
if x>0 and y>0:
    print('1')
elif x<0 and y>0:
    print('2')
elif x>0 and y<0:
    print('4')
else:
    print('3')


# for문

#15552_시간초과주의
import sys
t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)


# while문

#10951_try~except
import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break

#1110
# 사이클을 구할 수(n), 사이클을 계산하기 위한 임의의 수(new_n)
new_n = n = int(input())
cycle = 0
while True:
    ten = new_n//10 # 십의 자리수 할당
    one = new_n%10 # 일의 자리수 할당
    sum_two = ten+one #각 자릿수를 더한 수
    cycle+=1 #사이클 횟수
    # 원래 수의 일의자리, 더한 수의 일의자리 스트링으로 합친 후, 정수로 변환
    new_n = int(str(one)+str(sum_two%10))
    # 새로운 수가 첫번째 원래 수로 돌아오면 멈추기
    if (n == new_n):
        break
print(cycle)


# 1차원 배열

# 4344
c = int(input())
for i in range(c):
    student = 0
    score = list(map(int, input().split()))
    mean = sum(score[1:])/score[0]
    for j in score[1:]:
        if j > mean:
            student+=1
    ratio = student/score[0]*100
    print(('%.3f' % ratio)+'%')
