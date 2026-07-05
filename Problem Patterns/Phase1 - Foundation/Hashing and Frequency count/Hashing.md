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