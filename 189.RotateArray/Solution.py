# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for _ in range(k):
#             nums.insert(0, nums[-1])
#             del nums[-1]
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Try solving with modulor arithmatic in this atempt

        In this atempt imagine that indicies of array "nums" is like a clock. It an index goes out of bound then it come right back to the beginning if index goes out of bound in right direction, and visa versa in left direciton.

        We can store the new index of each element in a hash table, hash map, or dictionary.
        """
        new_index_map = {}
        for old_index, elem in enumerate(nums):
            new_index_map[(old_index + k) % len(nums)] = elem
        print(new_index_map)

        for new_index, elem in new_index_map.items():
            nums[new_index] = elem


s = Solution()
s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
