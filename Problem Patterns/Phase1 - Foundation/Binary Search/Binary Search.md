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
# Train of thought for 153. Find Minimum in Rotated Sorted Array
1. Use binary search.
2. There are 2 possibilities:
	1. The mid element is greater than the last element.
		1. This means that the smallest number can only be found between mid and last element.
	2. The mid element is smaller than the last element.
		1. This means that the smallest number can only be found in 1st half of the array.
3. left_ptr = 0
4. right_ptr = n - 1
5. While left_ptr < right_ptr:
	1. calculate mid = (left_ptr + right_ptr) // 2
	2. if `nums[mid]` == `nums[right_ptr]`:
		1. return `nums[mid]`
	3. if `nums[mid]` < `nums[right_ptr]`:
		1. right_ptr = mid
		2. continue
	4. left_ptr = mid + 1
6. return `nums[left_ptr]`
# Train of thoughts 875. Koko Eating Bananas
1. If koko has chosen a banana-per-hour speed, can she change her speed? No
2. Can she move on to next pile if she finishes early before whole hour is completed? No
3. If koko has decided a speed `k` and she has pile of `p` bananas, in how many hours can she finish? ceil number of k/p
4. Since, koko has multiple piles to finish, find and as I compute the time for each pile, I keep adding it to a variable so I can compare it with the time limit koko has.
5. Once I have the total time, I can check if koko has run out of find or not. 
6. If koko has run out of time then koko needs to be faster
7. If koko has still time to spare then koko can be slower.
8. Koko can eat with speed of  maximum of max of piles and minimum of 1.
9. 