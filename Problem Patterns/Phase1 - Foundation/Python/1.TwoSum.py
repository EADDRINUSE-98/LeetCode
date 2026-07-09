#!/bin/env python3
class Solution:
    def twosum(self, nums: list[int], target: int):
        nums_cache = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_cache:
                return [nums_cache[target - nums[i]], i]
            nums_cache[nums[i]] = i


if __name__ == "__main__":
    sol = Solution()
    result = sol.twosum([2, 7, 11, 15], 9)
    print(result)

    result = sol.twosum([3, 2, 4], 6)
    print(result)

    result = sol.twosum([3, 3], 6)
    print(result)
