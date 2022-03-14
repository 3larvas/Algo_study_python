# from typing import List
#
# def trap(heights : List[int]) -> int:
#     vol = 0
#     idx_l = 0
#     idx_r = len(heights) - 1
#     max_h_l = heights[idx_l]
#     max_h_r = heights[idx_r]
#
#     while idx_l < idx_r:
#         print(f'{idx_l} : {idx_r}')
#         max_h_l = max(max_h_l, heights[idx_l])
#         max_h_r = max(max_h_r, heights[idx_r])
#         if max_h_l < max_h_r:
#             vol += max_h_l - heights[idx_l]
#             idx_l += 1
#         else:
#             vol += max_h_r - heights[idx_r]
#             idx_r -= 1
#     return vol
#
#
# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

def aaa(num) :
    def bbb():
        global num
        num += 1
        print(num)
    bbb()
aaa(123)