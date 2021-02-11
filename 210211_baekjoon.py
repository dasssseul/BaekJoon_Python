# 2935
n1 = int(input())
operator = input()
n2 = int(input())
result = 0
if operator == '*':
    result = n1*n2
else:
    result = n1+n2
print(result)

# 9498
score = int(input())
if score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
elif score>=60:
    print('D')
else:
    print('F')

# 10817-1
n = list(map(int,input().split()))
n.remove(max(n))
n.remove(min(n))
print(n.pop(0))

# 10817-2
n = list(map(int, input().split()))
second_n = sorted(n)
print(second_n[1])

# 11653
n = int(input())
while n != 1:
    for i in range(2,n+1):
        if n%i == 0:
            print(i)
            n //= i
            break

# 1789
s = int(input())
result = 0
for i in range(4294967296):
    result += i
    if result == s:
        print(i)
        break
    elif result > s:
        print(i-1)
        break

