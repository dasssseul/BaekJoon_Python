
# 1번 문제

def solution(s):
    answer = 0
    number = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
              '9': 'nine'}
    for key, value in number.items():
        if value in s:
            s = s.replace(value, key)
    answer = s
    return answer

solution("23four5six7")
