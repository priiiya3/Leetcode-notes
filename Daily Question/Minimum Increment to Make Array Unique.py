# Day 20

# Leetcode Problem 945: Minimum Increment to Make Array Unique

# Problem Statement
"""
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
"""

# Approach:
"""
Khud se ni hua, Had to take help from discuccion. ek bande ne comment me likha tha:
To solve do : nums.sort() + Leetcode Problem 1827.

Problem 1827 Easy level Problem hai jisme array diya hai aur hme bas array ko increasing bnana hai and return karna hai ki kitne times array 
elements ko in-total increment karna pada. And we need to do this without changing the order of elements.
Simple hai, har step par bas check kro is nums[i] agar picche wale nums[i-1] se chhota hai to nums[i] ko nums[i-1] + 1 times badha do.
to wo nums[i-1] se badh jayega by 1. and har increment par cnt var me har dono ka difference add krtejao and end me cnt return krdo


Iss problem me bhi ham nums ko sort krenge pahle qki hme minimum steps me array ko increasign bnana hai. 
Baki after sorting copy paste same code as problem 1827.
"""

# Solution
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        # sort the array so that we perform increment in minimum step
        nums.sort()
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]: # agar current element picche wale se chhota hai
                diff = (nums[i-1] + 1) - nums[i] # here diff is the least value that, when added to nums[i], will make nums[i] > nums[i-1]
                nums[i] += diff
                cnt += diff
        
        return cnt
    
# Driver's Code
Result = Solution()

# Test Case
testcase1 = Result.minOperations(nums=[1, 2, 2])
print(testcase1) # expected: 1 (After 1 move, the array could be [1, 2, 3])

# Test Case
testcase2 = Result.minOperations([3,2,1,2,1,7])
print(testcase2) # expected: 6 (After 6 moves, the array could be [3, 4, 1, 2, 5, 7]. It can be shown with 5 or less moves that it is impossible for the array to have all unique values.)

