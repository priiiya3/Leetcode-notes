# Problem 3185: Count Pairs That Form a Complete Day II

# Statement:
"""
Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j where i < j and hours[i] + hours[j] forms a complete day.

A complete day is defined as a time duration that is an exact multiple of 24 hours.

For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.

 

Example 1:

Input: hours = [12,12,30,24,24]

Output: 2

Explanation: The pairs of indices that form a complete day are (0, 1) and (3, 4).

Example 2:

Input: hours = [72,48,24,3]

Output: 3

Explanation: The pairs of indices that form a complete day are (0, 1), (0, 2), and (1, 2).

 

Constraints:

1 <= hours.length <= 5 * 105
1 <= hours[i] <= 109
"""

# Approach:
"""
This Problem is similar to Problem 3185. Only diffrence is the contraints. 
Given the constraints (array length up to 10**9), the brute force approach is impractical. 
Instead, we can use a more efficient approach leveraging modular arithmetic and a hash map (or dictionary) to 
count occurrences of residues modulo 24. This approach has a time complexity of O(n).

# In this we need to see that even the residual can have sum of 24. 

1: Modular Arithmetic Insight:
    1.a: Two numbers 𝑎 and 𝑏 sum to a multiple of 24 if (a+b)%24 == 0
    1.b: This can be rephrased using modular arithmetic: (a%24 + b%24)%24 == 0
    1.c: Lets call a%24 and b%24 the 'residues' of a and b respectively

2: Residue Pair:
    2.a: For two residues to sum to 0 modulo 24, they must either both be 0, or one must be the complement of the other within 24.
    2.b: Example pairs of residues that sum to 24 (or 0 modulo 24):
      (0 + 0), (1 + 23), (2 + 22), ... (21 + 3)..up to (12 + 12).

3: Counting Residues:
    3.a: Use a dictionary to count how many times each residue appears in the array.
    3.b: For each number in the array, calculate its residue modulo 24 and update the dictionary.  

4: Finding Valid Pairs:

    4.a: For residue 0 and 12, pairs are formed within the same group (e.g., 0 pairs with 0, 12 pairs with 12).
    4.b: For other residues, pairs are formed between complementary residues (e.g., residue 1 pairs with residue 23).
    
This way we solve this problem with the time complexity of O(n).

Code me basically apne ko:
1: sabse pahle poore array ka residue cnt nikal k map me store kr lena hai

2: jin residues ki value 0 ya 12 hai, unke liye ham, [n*(n-1)]//2 karke saare pairs count kr lenge
    (for example: if mod=12 (have freq of 3), then number of pairs = [3*(3-1)]//2 = 3.
    AISA KYUU??????, 12 k liye (sum of n elements) wala formula kyu??..Because 12 multiplied with any number will give us a multiple of 24.
    So we want to consider sum of all n elements. Similar reason for mod==0 too.).

    3: and baaki residue values ko ham unke complimentary pairs se multiply krke saare possible pairs nikal lenge.
    (for example if mod == 1(having cnt 3), then uska complementry mod hua :24-1= 23(lets say 23 has cnt of 2)...so number of pairs are (cnt[1]*cnt[23])=3*2=6) 
"""

# Solution: 
from collections import defaultdict
from typing import List
class Solution:
    def countCompleteDayPairs(self, nums: List[int]) -> int:

        map = defaultdict(int)
        res = 0

        # Count the occurrences of each residue modulo 24
        for num in nums:
            residue = num%24
            map[residue] += 1

        # Calculate the number of valid pairs
        for mod in range(13): # Only need to check up to 12, because mod + (24 - mod) pairs
            n = map[mod]

            if mod == 0 or mod == 12:
                res += (n * (n-1))//2 # For mod 0 and 12, pairs are formed within the same group
            else:
                 # For other mods, pairs are formed between complementary groups
                res += (n * (map[24-mod]))

        return res

# Driver's Code
Ret = Solution()

# Test Case 1:
testcase1 = Ret.countCompleteDayPairs([12,12,30,24,24])
print(testcase1) # expected: 2

# Test Case 2:
testcase2 = Ret.countCompleteDayPairs([72, 48, 24, 3])
print(testcase2) # expected: 3

