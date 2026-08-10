#!/bin/env python3


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        rotated_first_elem_index = 0
        rotated_first_elem = nums[rotated_first_elem_index]
        sorted_nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_nums[mid] == rotated_first_elem:
                unrotated_first_elem_index = mid
                break
            if sorted_nums[mid] < rotated_first_elem:
                left = mid + 1
                continue
            right = mid - 1
        rotation_frequency = len(nums) - unrotated_first_elem_index
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_nums[mid] == target:
                target_index_sorted = mid
                break
            if sorted_nums[mid] < target:
                left = mid + 1
                continue
            right = mid - 1
        else:
            return -1
        target_index_rotated = (target_index_sorted + rotation_frequency) % len(nums)
        return target_index_rotated


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))
    print(sol.search([1], 0))
