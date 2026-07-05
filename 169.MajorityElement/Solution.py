# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         """Hash map approach"""
#         elem_count = {}
#         for elem in nums:
#             if elem not in elem_count.keys():
#                 elem_count[elem] = 1
#                 continue
#             elem_count[elem] += 1
#         for elem, count in elem_count.items():
#             if count > len(nums) // 2:
#                 return elem


# class Solution:
#     """Sorting approach"""
#
#     def majorityElement(self, nums: list[int]) -> int:
#         nums.sort()
#         return nums[len(nums) // 2]


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        res = count = 0
        for num in nums:
            if count == 0:
                res = num
            count += 1 if num == res else -1
        return res
