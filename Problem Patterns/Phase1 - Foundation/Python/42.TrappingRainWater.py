#!/bin/env python3

from collections import deque


class Solution:
    def trap(self, height: list[int]) -> int:
        max_right_heights = deque([])
        max_left_heights = deque([])
        total_trapped_rain = current_max_right = current_max_left = 0
        for i in range(len(height)):
            max_left_heights.append(current_max_left)
            current_max_left = max(current_max_left, height[i])

        for i in range(-1, -(len(height) + 1), -1):
            max_right_heights.appendleft(
                current_max_right
            )  # for O(1) time insertion from front.
            current_max_right = max(current_max_right, height[i])

        for i in range(len(height)):
            if min(max_left_heights[i], max_right_heights[i]) <= height[i]:
                total_trapped_rain += 0
                continue
            total_trapped_rain += (
                min(max_left_heights[i], max_right_heights[i]) - height[i]
            )
        return total_trapped_rain


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(sol.trap([4, 2, 0, 3, 2, 5]))
