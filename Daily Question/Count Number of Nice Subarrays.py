# Day 26

# Leetcode Problem: Count Number of Nice Subarrays
"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""

# Approach:
"""
Intuition
Since we only need to find the number of subarrays that contain a certain count of odd elements, we can ignore the numerical values of the elements and replace all odd values with 1 and even values with 0.

Now, all we need to do is identify sequences of elements within the array whose sum equals the number of odd elements needed to make a nice array. Solutions that require sequences of elements to meet criteria often utilize prefix sums, also sometimes referred to as cumulative sums.

Note: If you aren't aware of this concept we recommend you first solve this problem 560. Subarray Sum Equals K.

Utilizing prefix sums simplifies our approach and lets us avoid determining the sum of elements for every new subarray considered. Using the prefix sums approach, we can calculate the sum of elements between two indices, subtracting the prefix sum corresponding to the two indices to obtain the sum directly instead of iterating over the subarray to find the sum.

We'll use this approach to calculate how many odd numbers are between two indices in the array. Let's call the two indices start and end. If the number of odd numbers between start and end equals k, we have found a nice subarray. We will calculate this by finding the difference between the end and start indices.

Based on these thoughts, we use a hashmap to store the prefix sum of indices as keys and their frequency of occurrence as values. Instead of modifying nums, we can apply the modulo 2 operation when storing values in the hashmap.

We traverse the array nums to compute the prefix sum up to each element modulo 2. Each unique sum encountered is recorded in a hashmap. If a sum repeats, we increment its corresponding count in the hashmap. Also, for each sum encountered, we find the number of times sum - k has appeared before, as this count indicates how many subarrays with sum k exist up to the current index. We increase the count by that same amount.

Algorithm
Initialize integers currSum = 0,subarrays = 0 and a hashmap prefixSum.
Initialize prefixSum[0] with 1 to account for the initial value of currSum.
Iterate over all the elements of nums:
Compute currSum as currSum = currSum + nums[i] % 2.
If currSum - k exists in the hashmap:
Increment the value of subarrays with prefixSum[currSum - k].
Increment prefixSum[currSum] by 1.
Return subarrays.
"""

# Solution:
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        curr_sum = 0
        sub = 0
        prefix = {curr_sum: 1}
        
        for i in range(len(nums)):
            curr_sum += nums[i] % 2
            # print(curr_sum, "11")
            if curr_sum - k in prefix:
                sub += prefix[curr_sum-k]
                
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            
        return sub