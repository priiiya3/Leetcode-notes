# Problem 3184: Count Pairs That Form a Complete Day

# Problem Statement:
"""
Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j where i < j and hours[i] + hours[j] forms a complete day.

A complete day is defined as a time duration that is an exact multiple of 24 hours.

For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.

 

Example 1:

Input: hours = [12,12,30,24,24]

Output: 2

Explanation:

The pairs of indices that form a complete day are (0, 1) and (3, 4).

Example 2:

Input: hours = [72,48,24,3]

Output: 3

Explanation:

The pairs of indices that form a complete day are (0, 1), (0, 2), and (1, 2).

 

Constraints:

1 <= hours.length <= 100
1 <= hours[i] <= 109
"""

# Approach:
"""
We need to find all possible sums in array. We know Sum of n natural number sis [n*(n-1)]//2.

Since this was a Easy Problem and first question of the contest, Brute Force will work just fine here.

All we need to do is take 2 for loops and for every i < j just check if nums[i]+nums[j] % 24 == 0.
Here % sign gives remainder when (nums[i]+nums[j]) is divided by 24. If the remainder is zero that means, we have found one such set.

Keep count of all such sets and return.
"""

# Solution:
from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        
        cnt = 0 # var to store all possible sets
        for i in range(len(hours)):
            for j in range(i+1, len(hours)):
                if (hours[i]+hours[j]) % 24 == 0:
                    cnt += 1

        return cnt

# Driver's Code
Ret = Solution()

# Test Case 1:
testcase1 = Ret.countCompleteDayPairs([12,12,30,24,24])
print(testcase1) # expected: 2

# Test Case 2:
testcase2 = Ret.countCompleteDayPairs([72, 48, 24, 3])
print(testcase2) # expected: 3