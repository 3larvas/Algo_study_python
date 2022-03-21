from typing import List

nums = [-1, 0, 1, 2, -1, -4]

def sol_1(nums:List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    # range 범위 주의
    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-1):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1, len(nums)):
                if k > j+1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

    return result

def sol_2(nums:List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    for i in range(len(nums)-2):
        idx_l, idx_r = i+1, len(nums)-1
        if 0 < i and nums[i] == nums[i - 1]:
            continue
        while idx_l < idx_r:
            if nums[i] + nums[idx_l] + nums[idx_r] == 0:
                # 정답일 경우에 양쪽 인덱스 처리
                result.append([nums[i], nums[idx_l], nums[idx_r]])
                while idx_l < idx_r and nums[idx_l] == nums[idx_l+1]:
                    idx_l += 1
                while idx_l < idx_r and nums[idx_r] == nums[idx_r-1]:
                    idx_r -= 1
                idx_l += 1
                idx_r -= 1

            elif nums[i] + nums[idx_l] + nums[idx_r] > 0:
                idx_r -= 1
            else :
                idx_l += 1
    return result



print(sol_1(nums))
print(sol_2(nums))