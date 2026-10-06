#!/bin/env python3.14


class Solution:
    def max_consecutive_ones(self, s: str, k: int) -> int:
        n = len(s)
        if k >= n:
            return n
        left_ones = [0] * n
        count = 0
        for i in range(n):
            left_ones[i] = count
            if s[i] == 1:
                count += 1
            else:
                count = 0

        right_ones = [0] * n
        count = 0
        for i in range(n - 1, -1, -1):
            right_ones[i] = count
            if s[i] == 1:
                count += 1
            else:
                count = 0

        max_ones = 0
        for i in range(n - k + 1):
            j = i + k - 1
            total = left_ones[i] + k + right_ones[j]
            max_ones = max(max_ones, total)

        return max_ones
