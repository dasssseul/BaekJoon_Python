#1
print('Hello World!')

#2
a, b = map(int, input().split())
print(a+b)

#3
a, b = map(int, input().split())
print(a*b)

#4
a, b = map(int, input().split())
print(a-b)

#5
a, b = map(int, input().split())
print(a/b)

#6
a, b = map(int, input().split())
print(a+b, a-b, a*b, a//b, a%b, sep="\n")

#7
a, b, c = map(int, input().split())
print((a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c))%c, sep="\n")

#8
a = int(input())
b = int(input())
print(a+b)

#9
a = int(input())
b = list(map(int, input()))
ab1 = a*int(b[2])
ab2 = a*int(b[1])
ab3 = a*int(b[0])
print(ab1,ab2,ab3, sep="\n")
print(ab1+ab2*10+ab3*100)

#9_for문 활용 시
a = int(input())
b = list(map(int, input()))
rb = list(reversed(b))
f = []
for i in range(0,3):
    print(a*int(rb[i]))
    f.append(a*int(rb[i]))
sum = 0
for i in range(0,3):
    x = f[i]*(10**i)
    sum = sum+x
print(sum)

#9_for문 활용 시
a = int(input())
b = list(map(int, input()))

ab = [0, 0, 0]

for i in range(2, -1, -1) :
    ab[i] = a * int(b[i])
    print(ab[i])

print(ab[2]+ab[1]*10+ab[0]*100)

#10
R1, S = map(int, input().split())
R2 = 2*S-R1
print(R2)