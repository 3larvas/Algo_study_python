paragraph = 'babad'
# paragraph = '12328123454321'

def sol_1(para:str) -> str:
    # 함수안에 함수 선언해서 para변수를 전역변수처럼 사용 가능
    def expand(idx_l: int, idx_r: int) -> str:
        while idx_l >= 0 and idx_r <= len(para)-1 \
            and para[idx_l] == para[idx_r]:
            idx_l -= 1
            idx_r += 1
        print(f'idx_l : {idx_l}, idx_r : {idx_r}, result : {para[idx_l+1:idx_r]}')
        return para[idx_l+1:idx_r]

    result = ''
    for i in range(len(para)-1):
        print(f'---- i : {i} ----')
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result

print(sol_1(paragraph))