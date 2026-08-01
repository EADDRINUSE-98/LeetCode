# Train of thought for 704. Binary Search
1. Use 3 pointers. low, mid and high.
2. low starts at 0.
3. high starts at len(nums) -1.
4. mid should be the average of low + high.
5. while low =< high:
	1. mid = (low + high) // 2
	2. if `nums[mid]` == target:
		1. return mid
	3. if `nums[mid]` < target:
		1. move low to mid + 1.
		2. continue
	4. if mid == 0:
		1.  break
	5. move high to mid - 1.
6. return -1, if array is exhausted.
# Train of thought for 35. Search Insert Position
1. For this  low, high, and mid pointers will be used.
2. low starts at 0.
3. high starts at len(nums) - 1
4. While low <= high:
	1. mid = (low + high) // 2
	2. if `nums[mid]` == target:
		1. return mid
	3. if `nums[mid]` < target:
		1. move low to mid + 1.
		2. 
	4. elif mid == 0:
		1. break
	5. move high to mid - 1.
5. return low
# Train of thought for 34. Find First and Last Position of Element in Sorted Array
1. use 2 binary search.
2. binary search one will strictly find the leftmost range on target
3. binary search two will strictly find the rightmost range of target.