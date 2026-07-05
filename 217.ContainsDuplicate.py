#!/bin/env python3

# Brute force solution - Time limit exceeded
# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         for indx in range(len(nums)):
#             for second_indx in range(indx + 1, len(nums)):
#                 if nums[indx] == nums[second_indx]:
#                     return True
#         return False

# Hash map solution
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        For each `num` in `nums`. I'm checking if `num` is in `nums_set`. If it does return True if it does not add `num` in nums_set. Return False if entire `nums` is exhausted.
        """
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False


if __name__ == "__main__":
    sol = Solution()
    result = sol.containsDuplicate([1, 2, 3, 1])
    print(result)

    result = sol.containsDuplicate([1, 2, 3, 4])
    print(result)

    result = sol.containsDuplicate([1, 2, 3, 4])
    print(result)
