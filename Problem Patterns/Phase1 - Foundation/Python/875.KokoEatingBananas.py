#!/bin/env python3.14

from math import ceil
import unittest


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        current_min_speed = right
        while left <= right:
            mid = (left + right) // 2
            total_hours = 0
            for pile_size in piles:
                total_hours += ceil(pile_size / mid)

            if total_hours > h:
                left = mid + 1

            if total_hours <= h:
                current_min_speed = min(current_min_speed, mid)
                right = mid - 1
        return current_min_speed


class TestMinEatingSpeed(unittest.TestCase):
    def test_case_1(self):
        sol = Solution()
        self.assertEqual(sol.minEatingSpeed([3, 6, 7, 11], 8), 4)

    def test_case_2(self):
        sol = Solution()
        self.assertEqual(sol.minEatingSpeed([30, 11, 23, 4, 20], 5), 30)

    def test_case_3(self):
        sol = Solution()
        self.assertEqual(sol.minEatingSpeed([30, 11, 23, 4, 20], 6), 23)

    def test_case_4(self):
        sol = Solution()
        self.assertEqual(sol.minEatingSpeed([312884470], 312884469), 2)


if __name__ == "__main__":
    unittest.main()
