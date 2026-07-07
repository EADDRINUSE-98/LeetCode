#!/bin/env python3

# Brute force solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        For each `i` in range of 0 to `len(s)` or `len(t)`. Increment `s_count[s[i]]` and `t_count[t[i]]` by 1, end of loop. Then, for each `key` in `s_count`, return False if `s_count[key] != t_count[key]` else return True.
        """
        if len(s) != len(t):
            return False
        s_count = {}
        t_count = {}
        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            t_count[t[i]] = t_count.get(t[i], 0) + 1
        for key in s_count:
            if s_count.get(key) != t_count.get(key):
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    result = sol.isAnagram("anagram", "nagaram")
    print(result)

    result = sol.isAnagram("rat", "car")
    print(result)
