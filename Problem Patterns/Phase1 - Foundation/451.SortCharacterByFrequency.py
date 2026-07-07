#!/bin/env python3

# Too many for loops - solution 1
class Solution:
    def frequencySort(self, s: str) -> str:
        char_count_rec = {}
        for char in s:
            char_count_rec[char] = char_count_rec.get(char, 0) + 1
        sorted_count = sorted(
            [(count, char) for char, count in char_count_rec.items()], reverse=True
        )
        sorted_char_list = []
        for pair in sorted_count:
            count, char = pair
            for _ in range(count):
                sorted_char_list.append(char)
        return "".join(sorted_char_list)


# Solution 2 - but this got time limit exceed
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         char_count_rec = {}
#         for char in s:
#             count = (
#                 1
#                 if char_count_rec.get(char) is None
#                 else char_count_rec.get(char)[0] + 1
#             )
#             char_count_rec[char] = (count, "".join(char for _ in range(count)))
#         return "".join(
#             char_string
#             for _, char_string in sorted(list(char_count_rec.values()), reverse=True)
#         )


if __name__ == "__main__":
    sol = Solution()
    print(sol.frequencySort("tree"))
    print(sol.frequencySort("cccaaa"))
    print(sol.frequencySort("Aabb"))
