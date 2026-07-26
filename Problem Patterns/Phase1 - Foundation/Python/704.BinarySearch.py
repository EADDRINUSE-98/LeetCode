#!/bin/env python3


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
                continue
            high = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1, 0, 3, 5, 9, 12], 9))
    print(sol.search([-1, 0, 3, 5, 9, 12], 2))
    print(sol.search([1], 1))
    print(sol.search([1], 2))
    print(sol.search([1, 100], 100))
    print(sol.search([1, 100], 1))
    print(sol.search([1, 100], 2))
