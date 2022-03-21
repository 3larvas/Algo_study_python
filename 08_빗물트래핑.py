from typing import List

land = [0,1,0,2,1,0,1,3,2,1,2,1]

def sol_1(land:List[int]) -> int:
    idx_l, idx_r = 0, len(land)-1
    max_l, max_r, vol = 0, 0, 0
    while idx_l < idx_r:
        if land[idx_l] < land[idx_r]:
            if max_l > land[idx_l]:
                vol += max_l - land[idx_l]
            max_l = max(max_l, land[idx_l])
            idx_l += 1
        else:
            if max_r > land[idx_r]:
                vol += max_r - land[idx_r]
            max_r = max(max_r, land[idx_r])
            idx_r -= 1
    return vol

print(sol_1(land))