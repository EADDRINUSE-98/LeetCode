#!/bin/env python3.14

import unittest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price_recorded_day = max_profit_recorded = 0
        for current_day in range(len(prices)):
            if prices[current_day] <= prices[min_price_recorded_day]:
                min_price_recorded_day = current_day
                continue
            max_profit_recorded = max(
                max_profit_recorded,
                prices[current_day] - prices[min_price_recorded_day],
            )
        return max_profit_recorded


class TestMaxProfit(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([7]), 0)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([7, 6, 5, 4, 3, 2, 1]), 0)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([7, 6, 5, 4, 3, 1, 2]), 1)


if __name__ == "__main__":
    unittest.main()
