#!/bin/env python3


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        threesum_combinations = []
        nums_sorted = sorted(nums)
        for ptr1 in range(len(nums_sorted) - 2):
            ptr2 = ptr1 + 1
            ptr3 = len(nums_sorted) - 1
            if ptr1 > 0 and nums_sorted[ptr1] == nums_sorted[ptr1 - 1]:
                continue
            while ptr3 > ptr2:
                while (
                    ptr3 > ptr2
                    and nums_sorted[ptr1] + nums_sorted[ptr2] + nums_sorted[ptr3] != 0
                ):
                    while (
                        ptr3 > ptr2
                        and nums_sorted[ptr1] + nums_sorted[ptr2] + nums_sorted[ptr3]
                        > 0
                    ):
                        ptr3 -= 1
                    while (
                        ptr3 > ptr2
                        and nums_sorted[ptr1] + nums_sorted[ptr2] + nums_sorted[ptr3]
                        < 0
                    ):
                        ptr2 += 1
                if (
                    ptr3 > ptr2
                    and nums_sorted[ptr1] + nums_sorted[ptr2] + nums_sorted[ptr3] == 0
                ):
                    threesum_combinations.append(
                        [nums_sorted[ptr1], nums_sorted[ptr2], nums_sorted[ptr3]]
                    )
                ptr3 -= 1
                while ptr3 > ptr2 and nums_sorted[ptr3] == nums_sorted[ptr3 + 1]:
                    ptr3 -= 1
                ptr2 += 1
                while ptr3 > ptr2 and nums_sorted[ptr2] == nums_sorted[ptr2 - 1]:
                    ptr2 += 1
        return threesum_combinations


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    print(sol.threeSum([0, 1, 1]))
    print(sol.threeSum([0, 0, 0]))
    print(sol.threeSum([-4, -1, -1, 0, 1, 2]))
    print(sol.threeSum([-2, -2, 0, 2, 2]))
