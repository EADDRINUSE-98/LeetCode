# Train of thought for 125.ValidPalindrome
1. Pointer 1 - start at the beginning of the string and go forward.
2. Pointer 2 - start at the end of the string and go backward.
3. Run the logic while `pointer2 - pointer1` is greater than or equal to 1.  
4. Keep moving the 2 pointers in their appropriate directions.
5. Check if character at pointer1 and 2 are a member of alphanumeric.
	1. if yes, then go to step 6.
	2. if no, then move the appropriate pointer by 1 step as long as pointer reach an alphanumaric character.
	3. Do this separately for each pointer.
6. Check if character at pointer1 is equal to pointer2 character case-insensitively.
	1. if same, then move pointer by 1 step.
	2. if not same, return false
7. return true if while loop is ended.
# Train of thought for 167.TwoSum2-InputArrayIsSorted
1. Where should be the pointer 1 be? pointer 1 should be at the start of the array.
2. Where should be the pointer 2 be? at the end of the array.
3. While `numbers[ptr1] + numbers[ptr2] != target`:
	1. While sum of `numbers[ptr1]` and `numbers[ptr2]` is greater than target:
		1. Then move ptr2 left by 1 because if current elements sum goes higher than target then moving ptr1 right is pointless because it will only increase the sum.
	2. While sum of `numbers[ptr1]` and `numbers[ptr2]` is less than target:
		1. Then move ptr1 right by 1 because if current elements sum goes lower than target then moving ptr2 is pointless since it will only lower the sum.
4. return `[ptr1 + 1, ptr2 + 1]`
5. Here I don't need to check if `ptr2 > ptr1` because it is guaranteed that there will be a combination that will be satisfy the condition of 2 sum.
# Train of thought for 11.ContainerWithMostWater
1. Where should be the ptr1? at the start of the height array.
2. Where should be the ptr2? at the end of the height array.
3. Initialize `current_max_water_area = 0`, that will store the max area that  is encountered so far.
4. While `ptr2 > ptr1`:
	1. calulate `current_max_water_area = max(current_max_water_area, min(height[ptr2], height[ptr1]) * (ptr2 - ptr1))`.
	2. if height at ptr2 is less than or equal to height ptr1:
		1. Then, move ptr2 left by 1 step.
	3. else move ptr1 right by 1 step.
5. return `current_max_water_area`
6. I'm moving only that ptr that is less because even if I move the ptr with taller height, the limiting reagent of the area calculation will still be the smaller pillar and also moving closer to the smaller pillar will only decrease the area of the container. And if both pillar height is same then I can move whatever ptr, it won't matter at all.