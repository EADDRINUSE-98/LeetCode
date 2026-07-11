#!/bin/env python3


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        ptr1 = 0
        ptr2 = len(numbers) - 1
        while numbers[ptr2] + numbers[ptr1] != target:
            while numbers[ptr2] + numbers[ptr1] > target:
                ptr2 -= 1
            while numbers[ptr2] + numbers[ptr1] < target:
                ptr1 += 1
        return [ptr1 + 1, ptr2 + 1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
    print(sol.twoSum([2, 3, 4], 6))
    print(sol.twoSum([-1, 0], -1))
