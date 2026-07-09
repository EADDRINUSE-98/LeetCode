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