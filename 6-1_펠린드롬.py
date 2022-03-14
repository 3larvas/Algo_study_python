from collections import deque
import re

input_str = 'A man, a plan, a canal: Panama'

def sol_1(input_str:str)->bool:
    str_arr = []
    for char in input_str:
        if char.isalnum(): # 영어, 숫자
            str_arr.append(char.lower())
    while(len(str_arr)>1):
        if str_arr.pop(0) != str_arr.pop():
            return False
    return True

# deque를 활용하면 시간을 대폭 줄일 수 있다.
# 위 풀이에서 배열.pop(0)은 O(n)이지만, 데크.popleft 는 O(1)이다.
def sol_2(input_str:str)->bool:
    str_deq = deque()
    for char in str_deq:
        if char.isalnum():  # 영어, 숫자
            str_deq.append(char.lower())
    while (len(str_deq) > 1):
        if str_deq.pop != str_deq.pop():
            return False
    return True

def sol_3(input_str:str)->bool:
    input_str = input_str.lower()
    # 파이썬 정규식
    input_str = re.sub('[^a-z0-9]','' , input_str)
    print(input_str)
    # 파이썬 문자 슬라이싱
    return input_str == input_str[::-1]

# 파이썬 슬라이싱
S = '안녕하세요'
print(S[1:4]) # 녕하세
print(S[1:-2]) # 녕하
print(S[::-1]) # 요세하녕한
print(S[::2]) # 안하요 (2칸씩)

print(sol_1(input_str))
print(sol_2(input_str))
print(sol_3(input_str))