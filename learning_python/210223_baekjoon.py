# 1977
m = int(input())
n = int(input())
final = []
for i in range(101):
    if i*i >= m and i*i <=n:
        final.append(i*i)
if len(final) == 0:
    print(-1)
else:
    print(sum(final))
    print(min(final))

# 11098
n = int(input())
for i in range(n):
    p = int(input())
    c = {}
    for j in range(p):
        key, val = map(str,input().split())
        c[int(key)] = val
    m = max(c)
    print(c[m])

# 5635_넘어렵당ㅜ
n = int(input()) # 반에 있는 학생 수 입력 받기
student = [] # 이름, 생일을 넣을 리스트 선언
for i in range(n):
    s, d, m, y = input().split() # 이름, 생일(일, 월, 연도)입력받기
    if len(m) == 1: # 정렬을 위해 한자리수인 월 앞에 0 붙여주기
        m = '0'+m
    if len(d) == 1: # 정렬을 위해 한자리수인 일 앞에 0 붙여주기
        d = '0'+d
    student.append((s,y+m+d)) # 이름과 생일('연월일')을 묶어서 리스트에 넣어주기
student.sort(key=lambda x:int(x[1])) # 생일을 기준으로 오름차순 정렬
print(student[-1][0]) # 생일이 제일 느린 학생이 나이 가장 적음
print(student[0][0]) # 생일이 제일 빠른 학생이 나이 가장 많음

