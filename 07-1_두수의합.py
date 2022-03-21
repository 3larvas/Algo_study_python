from typing import List

nums = [7, 11, 15, 2]
target = 9

def sol_1(nums:List[int], target:int)->List[int]:
    # range 범위 헷갈리지 말 것.
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def sol_2(nums:List[int], target:int)->List[int]:
    for idx, val in enumerate(nums):
        comp = target - val
        if comp in nums[idx+1:]:
            return [nums.index(val), nums[idx+1:].index(comp)+(idx+1)]

def sol_3(nums:List[int], target:int)->List[int]:
    # idx 값을 dict에 저장해서 O(1)만에 탐색한다.
    nums_dict = {}
    for idx, val in enumerate(nums):
        nums_dict[val] = idx

    for idx, val in enumerate(nums):
        if target - val in nums_dict and idx != nums_dict[target-val]:
            return [idx, nums_dict[target-val]]

print(sol_1(nums,target))
print(sol_2(nums,target))
print(sol_3(nums,target))