# from typing import List
#
# def sum_num_1(nums: List[int], target: int) -> List[int]:
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             tmp = nums[i] + nums[j]
#             if tmp == target :
#                 return [i, j]
#
# def sum_num_2(nums: List[int], target: int) -> List[int]:
#     for idx, val in enumerate(nums):
#         complement = target - val
#         if complement in nums[idx+1:]:
#             return [idx, nums[idx+1:].index(complement) + (idx+1)]
#
# def sum_num_3(nums: List[int], target : int ) -> List[int]:
#     nums_map = {}
#     for idx, val in enumerate(nums):
#         nums_map[val] = idx
#     for idx, val in enumerate(nums):
#         if target - val in nums_map and idx != nums_map[target - val]:
#             return [idx, nums_map[target - val]]
#
#
#
# print(sum_num_2([2, 7, 11, 15], 9))
#


import requests
import json
url = 'https://new.land.naver.com/complexes/8349?ms=37.5044079,126.7402181,16&a=APT:ABYG:JGC&b=A1&e=RETAIL&g=45000&l=300'
# res  = requests.get(url)
# res = requests.post(url)

res = requests.get(url,data={"sameAddressGroup":"false"},headers={
    "Accept-Encoding": "gzip",
    "Host": "new.land.naver.com",
    "Referer": "https://new.land.naver.com/complexes/8928?ms=37.482968,127.0634,16&a=APT&b=A1&e=RETAIL",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
})
res.encoding = "utf-8-sig"
# temp=json.loads(res.text)
print(res.text)