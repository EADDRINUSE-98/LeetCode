#!/bin/env python3.14


class Solution:
    def max_equlized_split(self, s: str) -> int:
        n = len(s)
        cumulative = [0] * n
        zero_hits = 0
        current_balence = 0
        for indx, char in enumerate(s):
            current_balence += -1 if char == "L" else 1
            cumulative[indx] = current_balence
            if current_balence == 0:
                zero_hits += 1
        one_swap_can_be_done = False
        for indx in range(n - 1):
            if s[indx] == "L" and s[indx + 1] == "R" and cumulative[indx] == -2:
                one_swap_can_be_done = True
                continue
            if s[indx] == "R" and s[indx + 1] == "L" and cumulative[indx] == 2:
                one_swap_can_be_done = True
        return zero_hits + 1 if one_swap_can_be_done else zero_hits
