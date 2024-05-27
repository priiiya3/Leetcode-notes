# DAY 6
## Leetcoe Problem 1608: Special Array With X Elements Greater Than or Equal X

"""
Problem:
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

 

Example 1:

Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
Example 2:

Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.
Example 3:

Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""

##Approach

"""
I used a brute force aproach here. So we just need to find a number x that is less that x numbers.
So we know that:
1: minimum value of x will be 1 (This is because if x equals 0, the array nums must be empty, but the constraints guarantee that nums has at least 1 element.)
2: & the maximum value of x will be len(nums) ( This is because for an integer to be the answer, there must be at least that number of integers in nums. If we assume x to be nums.length + 1, there must be precisely nums.length + 1 integers in the array that are greater than or equal to x, but there are only nums.length integers in nums)

So simply start a loop from 1 (min value of x) to len(nums) (max value of x) and check if there exist x elemnets in arrray that are greater than x by simple search algorithm


Since we need to perform searching here, as we are searching for number of elements in array with value greater than x.
Any searching algorithm could be used, I used simple for loop and O(N) time complecxity 
which makes the overall time complexity of this soluttion O(N*N).

but a more better methid would be to used Binary search for the searching part. 
Binary search will make the complexity of this algorithm O(Nlog(n)).
"""

## SOLUTION:
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()

        def solve(nums, val):
            cnt = 0
            for i in range(len(nums)):
                if nums[i] >= val:
                    cnt += 1

            return cnt 


        for i in range(len(nums), 0, -1):
            
            
            value = solve(nums, i)
            # print(value, i)
            if value == i:
                return i

        return -1
    
# Driver's Code
result = Solution()

# TestCase 1
testcase1 = result.specialArray(nums=[0,4,3,0,4])
print(testcase1) # expected: 3

#TestCase 2
testcase2 = result.specialArray(nums=[3, 5])
print(testcase2) # # expected: 2

# TestCase 3
testcase3 = result.specialArray(nums=[0, 0])
print(testcase3) # # expected: -1