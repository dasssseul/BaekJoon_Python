# 함수

# 15596_정수 N개의 합_1
def solve1(a):
    ans = 0
    for i in a:
        ans+=i
    return ans

# 15596_정수 N개의 합_2
def solve2(a):
    return sum(a)


#4673_셀프 넘버
numbers = list(range(1,10001)) # 1~10000까지의 정수가 들어있는 리스트 생성
remove_list = [] # 셀프 넘버가 아닌 수를 넣을 리스트 정의
for i in numbers:
    for j in str(i): # 정수 i를 string으로 변형하여 각각 저장
        i += int(j) # int로 다시 변형하여 각 자릿수를 더해줌
    if i <= 10000:
        remove_list.append(i)
for remove_num in set(remove_list):
    numbers.remove(remove_num) # 중복 제거 후 전체 정수에서 셀프 넘버가 아닌 수 제거
for self_num in numbers:
    print(self_num)


#1065_한수_내코드...
numbers = list(range(100,1001))
hannum = list(range(1,100))
for i in numbers:
    find = []
    for j in str(i):
        find.append(int(j))
    for k in range(len(find)-2):
        if (find[k+1] - find[k]) == (find[k+2]-find[k+1]):
           hannum.append(i)
n = int(input())
result = 0
for i in hannum:
    if i <= n:
        result+=1
print(result)

#1065_한수_모범답안
n = int(input())
hansu = 0
for i in range(1,n+1):
    if i < 100: # 1~99는 모두 한수
        hansu+=1
    else:
        find = list(map(int,str(i)))
        if (find[0]-find[1]) == (find[1]-find[2]): # 등차 수열 체크
            hansu+=1
print(hansu)


# 문자열

#1152_단어의 개수
word = list(input().split())
print(len(word))


#5622_다이얼_너무어렵다ㅜ
phone = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
time = 0

for i in phone: #phone 리스트에서 요소 하나를 가져옴
    for j in i: #그 요소를 한 문자씩 쪼갬
        for k in word: #입력받은 문자를 하나씩 분리
            if j==k: #두 알파벳이 같다면
                time+=phone.index(i)+3
print(time)


#2941_크로아티아 알파벳_replace함수

alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
for i in alphabet:
    word = word.replace(i,'*') #word에 i와 동일한 문자가 있으면 '*'로 변환
print(len(word))