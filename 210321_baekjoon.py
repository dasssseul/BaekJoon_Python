# 10808
import string
alpha = string.ascii_lowercase
word = input()
for i in alpha:
    print(word.count(i),end=' ')

# 1157
word = input().upper()
set_word = list(set(word))
number = []
for i in set_word:
    number.append(word.count(i))
if number.count(max(number)) > 1:
    print('?')
else:
    print(set_word[number.index(max(number))])

# 5218
import string
alpha = list(string.ascii_lowercase.upper())
t = int(input())
for i in range(t):
    x, y = list(map(str, input().split()))
    n = []
    print('Distances: ', end='')
    for j in range(len(x)):
        if alpha.index(x[j]) <= alpha.index(y[j]):
            n.append(alpha.index(y[j])-alpha.index(x[j]))
        else:
            n.append(alpha.index(y[j]) + 26 - alpha.index(x[j]))
    for k in n:
        print('%d' % k, end= ' ')
    print()

# 9086
t = int(input())
for i in range(t):
    word = input()
    print(word[0]+word[len(word)-1])

# 11365
while True:
    solve = str(input())
    if solve == 'END':
        break
    else:
        print(solve[::-1])

# 11170
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    number = 0
    for j in range(n,m+1):
        string = str(j)
        number+=string.count('0')
    print(number)

# 11655
import string
alpha_lower= list(string.ascii_lowercase)
alpha_upper = list(string.ascii_uppercase)
s = list(input())
new_s = []
for i in s:
    n = 0
    if i in alpha_upper:
        n = alpha_upper.index(i) + 13
        if n > 25:
            n -= 26
        new_s.append(alpha_upper[n])
    elif i in alpha_lower:
        n = alpha_lower.index(i)+13
        if n > 25:
            n-=26
        new_s.append(alpha_lower[n])
    else:
        new_s.append(i)
for i in new_s:
    print(i,end='')

# 1676
n = int(input())
number = 1
count = 0
for i in range(1,n+1):
    number *= i
number = list(str(number))
for i in range(len(number)-1,-1,-1):
    if number[i] == '0':
        count+=1
    if number[i] != '0':
        break
print(count)
