from typing import List

nums = [1, 4, 3, 2]

def sol_1(nums:List[int])->int:
    nums.sort()
    return sum(nums[::2])

print(sol_1(nums))