#!/bin/env python3.14

import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) in [0, 1]:
        #     return len(s)
        left_end = max_substr_len = right_end = 0
        visited_chars = {}
        while right_end < len(s):
            if (
                s[right_end] in visited_chars
                and visited_chars.get(s[right_end]) >= left_end
            ):
                # if s[right_end] in s[right_end:right_end]:
                max_substr_len = max(max_substr_len, right_end - left_end)
                left_end = visited_chars.get(s[right_end]) + 1
            visited_chars[s[right_end]] = right_end
            right_end += 1
        return max(max_substr_len, right_end - left_end)


class TestLengthOfLongestSubstring(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring("bbbbb"), 1)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring("pwwkew"), 3)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring(""), 0)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring("     "), 1)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring("$%"), 2)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring("ccbbcc"), 2)


if __name__ == "__main__":
    unittest.main()
