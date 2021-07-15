
# 1874번. 스택 수열

n = int(input())
stack = []
cnt = 0
yes = True
result = []

for _ in range(n):
    number = int(input())
    while cnt < number:
        cnt += 1
        stack.append(cnt)
        result.append('+')
    if stack[-1] == number:
        stack.pop()
        result.append('-')
    else:
        yes = False

if not yes:
    print('NO')
else:
    print('\n'.join(result))
