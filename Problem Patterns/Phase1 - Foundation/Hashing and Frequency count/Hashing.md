# When to use hashing
- Is my solution repeatedly asking "have I seen this before?" or "does this exist?" by scanning/looping over and over, then use hash map.
- Make sure to understand what needs to be the key and what needs to be the value.
# Questions to ask your self
1. What am I finding?
2. Where do I find it?
# Train of thought
1. Is my solution scanning over and over? Then use hash map
2. At each step, what am I finding? Is it direct or derived from current element?
3. Where do I find it for the lookup to be O(1)? (Key)
4. What to retrieve? (Value)
5. if found, then what to do?
6. If not found, then what to do?
# Train of thought for 217.Contains Duplicate
1. Is my solution scanning over and over?
2. At each step, what am I finding? (Direct value)
3. Do I need to store extra value or just existence? (just existence) Then don't use data structure with key-value pair. Use linear data structure.
4. Do I need distinct values? (Yes) Use set.
5. How do I check? check membership.
6. if found return True.
7. if not found return False.
# Train of thought for 242. Valid Anagram
1. At each step, what am I finding? (Derived value)
2. Do I need to store just value or any extra value? (Need to store value and it's number of counts) Then use hash map.
3. Where do I find? (Key) current element in a string.
4. What will I find? (Value) count of current element in a string.
5. What will I derive? `s_count[element] - t_count[element]`
6. if derived value is `0` for all keys, return True.
7. if not, return False.
# Train of thought for 49. Group Anagrams
1. At each step, what am I finding? (Derived value) I will derive a sorted string for each string.
2. Do I need to store the string or any extra value? Yes I need to store string and it's corresponding list of strings that are anagrams of each other.
3. Where do I find? (Key) sorted string.
4. What will I retrieve? (Value) a list of string.
5. Now return, values of each key in list format .
- **Trigger sentence** - when a problem needs me to group items with some common property, but items are not identical - then I need to derive a value that can be a common property and use it as hash key.
# Train of thought for 347.TopKFrequentElements
1. At each step, what am I finding? (Derived value) Calculating counts of current element.
2. Do I need to store extra data or just current element? (extra data too) use hash map.
3. What do I find? (key) current element.
4. What I get? (value) count of current element so far.
	1. if found, increment in existing count.
	2. if not found, increment by from 0.
5. Make a tuple of (values, key) and reverse sort them. Now get first K elements of reverse sorted list and return the value at index 1.
6. Return a list of keys.
- **Trigger sentence** - after counting, I still need to keep the count and element together but also need to sort by count. therefore, using tuple (count, number) and will reverse sort it.
# Train of thought for 451.SortCharacterByFrequency
1. At each step, what do I find? (Derived value) Increase count of current character.
2. Do I need to store extra values or just the count? (Extra values).
3. Where do I find it? (Key) Character
4. What do I get? (Value) count of key.
5. Now create a list of tuple (count, character) format and reverse sort it.
6. Now for each tuple in list of tuple, separate count and character, then for count times append that character is sorted_string_list.
7. then join all elements in sorted_string_list.
- Trigger - After counting, I still need to know what is the character that has post and least count for that use tuple.