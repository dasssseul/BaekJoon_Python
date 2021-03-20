# 1357
def Rev(x):
    return int(str(x)[::-1])
a, b = map(int, input().split())
print(Rev(Rev(a)+Rev(b)))

# 10987
find = ['a','e','i','o','u']
n = 0
word = list(input())
for i in word:
    if i in find:
        n+=1
print(n)

# 4458
n = int(input())
for i in range(n):
    word = str(input())
    word = word[0].upper()+word[1:]
    print(word)

# 11654
n = input()
print(ord(n))

# 11720
n = int(input())
number = list(map(int, input()))
print(sum(number))

# 11721
word = input()
for i in range(0,len(word),10):
    print(word[i:i+10])

# 10821_1
s = list(map(int, input().split(",")))
print(len(s))

# 10821_2
print(len(input().split(',')))