# Day 35

# Leetcode Problem 1509: Minimum Difference Between Largest and Smallest Value in Three Moves

# Problem Statement:
"""
You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

 

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 2 to 3. nums becomes [5,3,3,4].
In the second move, change 4 to 3. nums becomes [5,3,3,3].
In the third move, change 5 to 3. nums becomes [3,3,3,3].
After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: We can make at most 3 moves.
In the first move, change 5 to 0. nums becomes [1,0,0,10,14].
In the second move, change 10 to 0. nums becomes [1,0,0,0,14].
In the third move, change 14 to 1. nums becomes [1,0,0,0,1].
After performing 3 moves, the difference between the minimum and maximum is 1 - 0 = 1.
It can be shown that there is no way to make the difference 0 in 3 moves.
Example 3:

Input: nums = [3,100,20]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 100 to 7. nums becomes [3,7,20].
In the second move, change 20 to 7. nums becomes [3,7,7].
In the third move, change 3 to 7. nums becomes [7,7,7].
After performing 3 moves, the difference between the minimum and maximum is 7 - 7 = 0.
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# Approach:
"""
Easy approach. hame mainly minimum diffrence return karna hai. aur yha bola hai replace with any value, 
which basically means ki sabse largest/ ya smallest value ko ham delete krke minimize kar rhe sum.

Ye minimum sum paane ka 4 cases hai. Pahle ham array sort karenge phir:
1: Removing the three largest elements.
2: Removing the two largest and one smallest elements.
3: Removing one largest and two smallest elements.
4: Removing the three smallest elements

"""

# Solution:
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 4:
            return 0
        
        nums.sort()

        mini = float('inf')

        for left in range(4):
            right = n - 4 + left
            mini = min(mini, nums[right]-nums[left])

        return mini
    
# Driver's Code:
Result = Solution()

# Test Case 1:
testcase1 = Result.minDifference([5, 3, 2, 4])
print(testcase1) # expected: 0

# Test Case 2:
testcase2 = Result.minDifference([1,5,0,10,14])
print(testcase2) # expected: 1