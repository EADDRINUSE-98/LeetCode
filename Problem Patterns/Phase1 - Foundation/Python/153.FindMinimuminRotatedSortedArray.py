#!/bin/env python3.14


class Solution:
    def findMin(self, nums: list[int]) -> int:
        left_ptr = 0
        right_ptr = len(nums) - 1
        mid = 0
        while left_ptr < right_ptr:
            mid = (left_ptr + right_ptr) // 2
            if nums[right_ptr] == nums[mid]:
                return nums[mid]
            elif nums[mid] < nums[right_ptr]:
                right_ptr = mid
                continue
            left_ptr = mid + 1
        return nums[left_ptr]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([3, 4, 5, 1, 2]))
    print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(sol.findMin([11, 13, 15, 17]))
    print(sol.findMin([11]))
    print(sol.findMin([13, 11]))
    print(sol.findMin([3, 1, 2]))
