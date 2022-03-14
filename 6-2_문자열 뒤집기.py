from typing import List

input = ["h", "e", "l", "l", "o"]
print(id(input))

# 투포인트 풀이법
def sol_1(input_str : List[str]) -> List[str]:
    print(id(input_str))
    idx_left, idx_ritght = 0, len(input_str)-1
    while(idx_left<idx_ritght):
        input_str[idx_left], input_str[idx_ritght] = input_str[idx_ritght], input_str[idx_left]
        idx_left += 1
        idx_ritght -= 1
    return input_str

# 파이썬스러운 풀이법
def sol_2(input_str : List[str]) -> List[str]:
    print(id(input_str))
    # input_str[:] = input_str[::-1]
    input_str.reverse()
    # 몇몇 플랫폼에선 아래 타입이 컴파일 안될수도있다.
    # input_str = input_str[::-1]
    return input_str

print(sol_1(input))
print(sol_2(input))