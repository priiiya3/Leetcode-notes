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
# VISIT AGAIN

## CHATGOT Explanation:
"""
Sure, let's break down the code you provided, which calculates the number of subarrays whose sums are divisible by a given integer \( k \).

### Code Explanation

```python
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
            print(counts, num, currSum, currSum % k, res)
            
            counts[currSum % k] += 1

        return res
```

### Detailed Explanation

1. **Initialization**:
    ```python
    counts = Counter()
    currSum = 0
    res = 0
    ```
    - `counts`: A counter to keep track of the frequency of each remainder when the cumulative sum is divided by \( k \).
    - `currSum`: A variable to store the cumulative sum of the elements of the array as we iterate through it.
    - `res`: A variable to store the total count of subarrays whose sum is divisible by \( k \).

2. **Iterate Through the Array**:
    ```python
    for num in nums:
        currSum += num
        
        if currSum % k == 0:
            res += 1 
            
        res += counts[currSum % k]
        print(counts, num, currSum, currSum % k, res)
        
        counts[currSum % k] += 1
    ```
    - For each element `num` in the array `nums`:
      - Update `currSum` by adding the current element `num`.
      - Check if the current cumulative sum (`currSum`) is directly divisible by \( k \). If it is, increment `res` by 1 because the subarray from the start to the current element forms a valid subarray.
      - Add to `res` the number of times the current remainder (`currSum % k`) has been seen before. This is because if the remainder has been seen before, it means there is a subarray that, when removed, results in a sum that is divisible by \( k \).
      - Print the current state for debugging purposes, showing the `counts` dictionary, current `num`, `currSum`, current remainder (`currSum % k`), and the current value of `res`.
      - Update the `counts` counter for the current remainder (`currSum % k`).

3. **Return the Result**:
    ```python
    return res
    ```
    - Finally, return the total count of subarrays whose sum is divisible by \( k \).

### Key Concepts

- **Remainders and Cumulative Sums**: The use of remainders to track cumulative sums helps identify subarrays whose sums are divisible by \( k \). If the remainder of a cumulative sum modulo \( k \) has been seen before, it indicates that there is a subarray that contributes to the desired property.
- **Counter for Frequencies**: The `Counter` from the `collections` module efficiently keeps track of the number of times each remainder has occurred, which helps in counting the valid subarrays.

### Example Walkthrough

Let's go through a quick example to illustrate how the code works:

Assume `nums = [4, 5, 0, -2, -3, 1]` and `k = 5`.

- **Step-by-step iteration**:
  - `currSum = 4`: Remainder is `4 % 5 = 4`. No subarray found yet, `counts = {4: 1}`, `res = 0`.
  - `currSum = 9`: Remainder is `9 % 5 = 4`. `counts[4] = 1`, increment `res` by 1. Now `counts = {4: 2}`, `res = 1`.
  - `currSum = 9`: Remainder is `9 % 5 = 4`. `counts[4] = 2`, increment `res` by 2. Now `counts = {4: 3}`, `res = 3`.
  - `currSum = 7`: Remainder is `7 % 5 = 2`. No new subarray found, `counts = {4: 3, 2: 1}`, `res = 3`.
  - `currSum = 4`:
   Remainder is `4 % 5 = 4`. `counts[4] = 3`, increment `res` by 3. Now `counts = {4: 4, 2: 1}`, `res = 6`.
  - `currSum = 5`: Remainder is `5 % 5 = 0`. This is directly divisible by 5, increment `res` by 1. `counts[0] = 1`, `res = 7`.

By the end, `res` contains the total number of subarrays whose sum is divisible by \( k \), which would be the output of the function.
"""