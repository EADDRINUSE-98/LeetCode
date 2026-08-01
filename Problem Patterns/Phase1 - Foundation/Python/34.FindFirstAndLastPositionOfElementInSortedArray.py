#!/bin/env python3
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        low = 0
        high = len(nums) - 1
        leftmost = -1
        # for leftmost target index
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                leftmost = mid
                high = mid - 1
                continue
            if nums[mid] < target:
                low = mid + 1
                continue
            high = mid - 1
        low = 0
        high = len(nums) - 1
        rightmost = -1
        # for rightmost target index
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                rightmost = mid
                low = mid + 1
                continue
            if nums[mid] < target:
                low = mid + 1
                continue
            high = mid - 1
        return [leftmost, rightmost]


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))
    print(sol.searchRange([], 0))
