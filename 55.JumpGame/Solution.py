# class Solution:
#     def canJump(self, nums: list[int]) -> bool:
#         i = 0
#         while i < len(nums) - 1:
#             if nums[i] == 0:
#                 break
#             i += nums[i]
#
#         reached_end = True if i == len(nums) - 1 else False
#         return reached_end


# greedy approach
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        Example list - [3,1,2,0,4]
        take two pointers:
            i = index for current element
            g = goal index
        """
        g = len(nums) - 1
        i = g - 1
        while i >= 0:
            if nums[i] + i >= g:
                g = i
            i -= 1
        return True if g == 0 else False
