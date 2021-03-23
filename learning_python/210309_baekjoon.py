# 2908
n1, n2 = input().split()
n1 = list(n1)
n2 = list(n2)
if (n1[2]+n1[1]+n1[0]) > (n2[2]+n2[1]+n2[0]):
    print(n1[2]+n1[1]+n1[0])
else:
    print(n2[2]+n2[1]+n2[0])

# 2908_간단하게...
n1, n2 = input().split()
if (n1[::-1]) > (n2[::-1]):
    print(n1[::-1])
else:
    print(n2[::-1])

# 2460
number = 0
train = []
for i in range(10):
    off, on = map(int, input().split())
    number += on
    number -= off
    train.append(number)
print(max(train))

# 2577
a = int(input())
b = int(input())
c = int(input())
abc = list(map(int, str(a*b*c)))
for i in range(10):
    print(abc.count(i))

# 2592
sum_n = 0
number = []
max_count = 0
mod_num = 0
for i in range(10):
    n = int(input())
    sum_n += n
    number.append(n)
for j in number:
    if number.count(j) > max_count:
        max_count = number.count(j)
        mod_num = j
print(int(sum_n/10))
print(mod_num)

# 2711
t = int(input())
for i in range(t):
    pos, word = input().split()
    pos = int(pos)
    print(word[:pos-1],word[pos:],sep='')
