# Day 35

# Leetcode Problem 350: Intersection of Two Arrays II

# Problem Statement
"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

# Approach:
"""
Mujhe easiest approach ye laga ki main pahle ek hashmap me first array k har element ki frequency store karlu
Phir second array me traverse krke check karu ki second array ka elment i, kya mere hashmap me hai, agar hai to 
add it into my res array
"""

# Solution:
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1): return self.intersect(nums2, nums1)
        
        cnt = Counter(nums1)
        res = []
        for i in range(len(nums2)):
            if cnt[nums2[i]] > 0:
                res.append(nums2[i])
                cnt[nums2[i]] -= 1
                
        return res

# Driver's Code:
Result = Solution()

# Test Case 1:
testcase1 = Result.intersect(nums1 = [1,2,2,1], nums2 = [2,2])
print(testcase1) # expected: [2, 2]

# Test Case 2:
testcase2 = Result.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
print(testcase2) # expected: [4, 9]
