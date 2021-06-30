
# 20052번. 괄호 문자열 ?

s = input()
m = int(input())
cnt_array= []
partsum_array = []
partsum = 0
result = 0
for i in s:
    if i =='(':
        cnt_array.append(1)
    else:
        cnt_array.append(-1)
for j in range(m):
    partsum += cnt_array[j]
    partsum_array.append(partsum)
for k in range(m):
    a, b = map(int, input().split())
    if min(partsum_array[a-1:b])-partsum_array[a-2] >= 0:
        result += 1
print(result)
