
# 백준 단계별로 풀어보기
# 이진 탐색(binary search)


# 1920번. 수 찾기

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
numbers = list(map(int, input().split()))

start = 0
end = len(a)-1

def binary_search(a, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if target == a[mid]:
            return 1
        elif target < a[mid]:
            end = mid-1
        else:
            start = mid+1
    return 0

for i in numbers:
    result = binary_search(a, i, start, end)
    print(result)



# 10816번. 숫자카드2

from bisect import bisect_left, bisect_right

n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
sanggen = list(map(int, input().split()))

def count(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index

for i in sanggen:
    result = count(card, i, i)
    print(result, end=" ")



    
