#!/bin/env python3.14

from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        possible_speed = [speed for speed in range(1, max(piles) + 1)]
        total_hours = 0
        left = 0
        right = len(piles) - 1
        current_min_speed = 0
        while left <= right:
            mid = (left + right) // 2
            for pile_size in piles:
                total_hours += ceil(pile_size / possible_speed[mid])

            if total_hours > h:
                left = mid + 1

            if total_hours <= h:
                current_min_speed = min(current_min_speed, possible_speed[mid])
                right = mid - 1
        return current_min_speed


if __name__ == "__main__":
    sol = Solution()
    ## create test case using unittest
