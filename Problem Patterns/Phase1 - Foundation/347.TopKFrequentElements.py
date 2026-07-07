#!/bin/env python3


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_count_record = {}
        for num in nums:
            num_count_record[num] = num_count_record.get(num, 0) + 1
        sorted_by_count = sorted(
            [(value, key) for key, value in num_count_record.items()], reverse=True
        )
        frequent_element_list = []
        for i in range(k):
            frequent_element_list.append(sorted_by_count[i][1])

        return frequent_element_list


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(sol.topKFrequent([1], 1))
    print(sol.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))
