#!/bin/env python3.14


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_window_size = 1
        window_start = 0
        window_end = window_start + 1
        visited_char_rec = {s[window_start]: 1}
        while window_end < len(s):
            if s[window_end] in 


