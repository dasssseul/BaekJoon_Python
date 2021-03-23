# 5063
n = int(input())
for i in range(n):
    r,e,c = map(int, input().split())
    if r < e-c:
        print('advertise')
    elif r == e-c :
        print('does not matter')
    else:
        print('do not advertise')

# 10102
n = int(input())
vote = list(input())
if vote.count('A') > vote.count('B'):
    print('A')
elif vote.count('A') == vote.count('B'):
    print('Tie')
else:
    print('B')

# 10886
n = int(input())
cute = []
for i in range(n):
    cute.append(int(input()))
if cute.count(1) > cute.count(0):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
    
# 10988_첫시도(왜틀렸을까..)
word = list(input())
check = 1 #check를 0으로 하면 틀린다...(다솔이 찾아냄)
for i in range(len(word)//2):
    if word[i] != word[len(word)-1-i]:
        check = 0
        break
    if word[i] == word[len(word)-1-i]:
        check = 1
print(check)
    
# 10988
word = list(input())
reversed_word = list(reversed(word))
if word == reversed_word:
    print(1)
else:
    print(0)
