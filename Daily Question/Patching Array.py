# Day 22
# Leetcode Problem 330: Patching Array

# Similar Problem: Minimum Number of Coins to be Added (https://leetcode.com/problems/minimum-number-of-coins-to-be-added/description/)

# Problem Statement:
"""
Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.

 

Example 1:

Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
nums is sorted in ascending order.
1 <= n <= 231 - 1
"""

# Approach:
"""
The question asked for the "minimum number of patches required". In other words, it asked for an optimal solution. Lots of problems involving optimal solution can be solved by dynamic programming and/or greedy algorithm. I started with greedy algorithm which is conceptually easy to design. Typically, a greedy algorithm needs selection of best moves for a subproblem. So what is our best move?

Think about this example: nums = [1, 2, 3, 9]. We naturally want to iterate through nums from left to right and see what we would discover. After we encountered 1, we know 1...1 is patched completely. After encountered 2, we know 1...3 (1+2) is patched completely. After we encountered 3, we know 1...6 (1+2+3) is patched completely

Suppose we already have a collection of positive integers A, B, C, ..., M that can cover a range of [1, k] inclusive by selectively summing up some elements in our collection. We know that k must be the total sum of all elements in our collection.

Let's take in a new integer N = k+1 into our collection. We know without thinking that we can cover a range of [1, (k+1)] now, but is that all? No! Instead we claim that we can cover a range of [1, (k+1)+k] now. Why? Let's list all the numbers we have to cover between range [(k+1)+1, (k+1)+k] to make such claim true:

(k+1) + 1
(k+1) + 2
(k+1) + 3
(k+1) + ...
(k+1) + k

Focus on the highlighted addends. They simply form a range of [1, k], which is already covered by our original collection A, B, C, ..., M. 
And the other addend k+1 is merely our new member N we just took it.

So in summary, if we can already cover range [1, k], then by just taking in the next integer k+1, we will be able to cover a new range [1, k+(k+1)] inclusive.
There is no need to investigate all the numbers falling in between one by one as explained above.

Once you understand this, the rest would be quite simple.

For example, when we already have a coverage of [1, k-1]. What would be our best choice in order to cover k? 
No doubt, our best choice would be k itself. Because choosing any integer greater than k would not help. 
On the other hand, if we choose an integer smaller than k, let's say we choose j and j < k. We can write it as k = j + P, P is a positive integer. 
So from the above proof, we know that if we choose j, our new coverage would be [1, (k-1)+j]. But if we choose k itself, our new coverage would be 
[1, (k-1)+k], and (k-1)+k = (k-1)+(j+P) = ((k-1)+j) + P, 
which means we will have greater coverage by choosing k instead of j. 
Since j can be any positive integer smaller than k.
"""

# Solution:
# Mine written solution gave TLE. Better one is yet to understand