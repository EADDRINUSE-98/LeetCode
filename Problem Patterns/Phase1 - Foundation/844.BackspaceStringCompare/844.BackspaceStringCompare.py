#!/bin/env python3.14

from collections import deque


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = deque()
        for char in s:
            if char != "#":
                stack_s.append(char)
                continue
            elif len(stack_s) == 0:
                continue
            stack_s.pop()

        stack_t = deque()
        for char in t:
            if char != "#":
                stack_t.append(char)
                continue
            elif len(stack_t) == 0:
                continue
            stack_t.pop()
        # print(stack_s, stack_t)

        return stack_s == stack_t


if __name__ == "__main__":
    sol = Solution()
    print(sol.backspaceCompare("ab#c", "ad#c"))
    print(sol.backspaceCompare("ab##", "c#d#"))
    print(sol.backspaceCompare("a#c", "b"))
    print(sol.backspaceCompare("#b", "#b#b"))
