#!/bin/env python3


class Solution:
    def maxArea(self, height: list[int]) -> int:
        ptr1 = 0
        ptr2 = len(height) - 1
        current_max_container_area = 0
        while ptr2 > ptr1:
            current_max_container_area = max(
                current_max_container_area,
                min(height[ptr1], height[ptr2]) * (ptr2 - ptr1),
            )
            if height[ptr2] <= height[ptr1]:
                ptr2 -= 1
            else:
                ptr1 += 1
        return current_max_container_area


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(sol.maxArea([1, 1]))
