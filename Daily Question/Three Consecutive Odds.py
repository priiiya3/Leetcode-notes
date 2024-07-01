# Day 34

# Leetcode Problem 1550: Three Consecutive Odds

# Problem Statement
"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
"""

# Approach:
"""
Since this is a Easy level problem and contraints are not too large. 
I am gonna simply loop through the array and find the i, i+1 and i+2 element who are odd.
Time complexity is O(N) and Space Complexity is O(1).
"""

# Solution:
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        for i in range(len(arr)-2):
            if arr[i]%2 and arr[i+1]%2 and arr[i+2] % 2:
                return True
            
        return False

# Dirver's Code
Result = Solution()

# Test Case 1:
testcase1 = Result.threeConsecutiveOdds(arr = [2, 6, 4, 1])
print(testcase1) # expected: False

# Test Case 2:
testcase2 = Result.threeConsecutiveOdds(arr = [1,2,34,3,4,5,7,23,12])
print(testcase2) # expected: True