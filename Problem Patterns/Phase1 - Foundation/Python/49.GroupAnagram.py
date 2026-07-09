#!/bin/env python3


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_hash_record = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if anagram_hash_record.get(sorted_string) is None:
                anagram_hash_record[sorted_string] = []
            anagram_hash_record.get(sorted_string).append(string)
        return list(anagram_hash_record.values())


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

    print(sol.groupAnagrams([""]))

    print(sol.groupAnagrams(["a"]))
