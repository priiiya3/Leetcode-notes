## DAY 1
## Leetcoe Problem 78: Subset

"""Question:
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique."""

## Solution
"""
Approach: We can use Backtracking to generate all possible subset.
For the first element, we can start building subsets in two ways:

1. Include the current element in the subset and continue choosing other elements: Add the element to the subset, call generateSubsets with the next element, and then remove the element from the subset so we can explore other subsets.
2. Not include the element in the subset and continue choosing other elements: Call generateSubsets with the next element.

"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # we just need to return all possible subsets
        def recursion(nums, i, curr_subset, final_subset):
            # base condition
            if i == len(nums):
                final_subset.append(curr_subset[::]) # add subset so far made to final_subset
                return

            # when current element is taken into subset
            curr_subset.append(nums[i])
            recursion(nums, i+1, curr_subset, final_subset)

            # when current element is not taken into subset
            curr_subset.pop() # removing the nums[i] we added
            recursion(nums, i+1, curr_subset, final_subset)


        res_set = []
        recursion(nums, 0, [], res_set)
        
        return res_set


# Driver's code   
ques = Solution()
result = ques.subsets([1, 2, 3])
print(result)