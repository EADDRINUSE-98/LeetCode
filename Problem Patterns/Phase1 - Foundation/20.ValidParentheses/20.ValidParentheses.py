#!/bin/env python3.14

from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        parentheses = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = deque()
        for p in s:
            if p in parentheses:
                stack.append(p)
                continue
            elif p not in parentheses and len(stack) == 0:
                return False
            elif parentheses.get(stack[-1]) == p:
                stack.pop()
                continue
            stack.append(p)
        return True if len(stack) == 0 else False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))
    print(sol.isValid("()[]{}"))
    print(sol.isValid("(]"))
    print(sol.isValid("([])"))
    print(sol.isValid("([)]"))
    print(sol.isValid("(])"))
    print(sol.isValid("]()"))
    print(sol.isValid(")("))
