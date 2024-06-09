# Day 15
# Leetcode Problem 974: Subarray Sums Divisible by K

# Problem Statement:
"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104
"""

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        counts = Counter()
        currSum = 0
        res = 0
        
        for num in nums:
            currSum += num
            
            if currSum % k == 0:
                res += 1 
                
            res += counts[currSum % k]
            print(counts, num, currSum, currSum%k, res)
            
            counts[currSum % k] += 1

        return res
