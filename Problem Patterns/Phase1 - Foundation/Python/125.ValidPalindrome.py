#!/bin/env python3


from string import ascii_letters, digits


class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_string = ascii_letters + digits
        ptr1 = 0
        ptr2 = len(s) - 1
        while ptr2 > ptr1:
            while s[ptr1] not in alphanumeric_string and ptr2 > ptr1:
                ptr1 += 1
            while s[ptr2] not in alphanumeric_string and ptr2 > ptr1:
                ptr2 -= 1
            if s[ptr1].lower() != s[ptr2].lower():
                return False
            ptr1 += 1
            ptr2 -= 1

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print(sol.isPalindrome("race a car"))
    print(sol.isPalindrome(" "))
    print(sol.isPalindrome(",,,"))
