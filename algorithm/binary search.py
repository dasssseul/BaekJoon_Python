
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



    
# 2805번. 나무 자르기

import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

# 이진 탐색을 위한 시작점, 끝점, 높이 설정
start ,end, result = 0, max(tree), 0


# 이진 탐색 수행(반복문 활용)
while (start <= end):
    total = 0
    mid = (start+end)//2
    for i in tree:
        # 절단기 높이보다 큰 나무의 경우 잘린 높이 계산
        if i > mid:
            total += i-mid
    # 나무의 양이 부족한 경우 왼쪽 부분 탐색
    if total < m:
        end = mid - 1
    # 나무의 양이 충분한 경우 오른쪽 부분 탐색
    else:
        # 최대한 덜 잘랐을 때가 정답
        result = mid
        start = mid + 1

print(result)




