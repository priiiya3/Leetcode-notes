# Day 3
# Leetcode Problem 2597: The Number of Beautiful Subsets

"""
Problem Statement:
You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].
 

Constraints:

1 <= nums.length <= 20
1 <= nums[i], k <= 1000
"""

## My Approach
"""
We are going to use Bitwise + Recursion.


Apan karenge kya ki bits ka use krenge pta karne k liye ki konsa element subset me present hai
and konsa nhi.
So simply jo element 1 (set)  hai wo present hai jo 0 (unset) hai wo absent.

For Example: nums = [1, 2, 3, 4, 5, 6] and let its subset be [1, 2, 6]
then in bitwise I can represent the corresonding "mask" of [1, 2, 6] as : 100011.
(yha 1 sbse last digit hoga bits me and 6 first qki apan bits me right to Left read karte hai)



So overall we will simply traverse array from 0 to n. For each nums[i] to be in beautiful subset we will check: 
1: that nums[i] is not already present in mask. We do that using (1 << i) & mask. (here 1 << i makes the i'th bit 1 and &mask checks if that i'th bit is 1 in mask as well. 
    [(1<<i)&mask will return 1 if both are 1 or, can say, if nums[i] alreadyin mask])
2: That nums[i] - all currently present element in subset !=  diff. (Cause if they equal to diff, they are not beautiful)


After that if above two conditions satisfies, we will simple take two conditions that we allways take while forming subsets from array.
1: 'Take' current nums[i] in subset: (this we will do only is nums[i] is not making the array ugly i.e, is_beatiful = True)
    [take = find_subsets(nums, diff, index+1,  mask + (1 << index)) if is_Beautiful == True else 0]
2: 'Skip' current element by not including it in mask and simply moving to next index
    [take = find_subsets(nums, diff, index+1,  mask)]
"""

## Solution:
from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        def find_subsets(nums, diff, index, mask):
            if index == len(nums):
                return 1 if mask > 0 else 0

            is_Beautiful = True

            for i in range(index):
                # check that current element is not in mask and its difference != k
                # coz then only its beautiful
                if ((1 << i) & mask) == 0 or (abs(nums[index] - nums[i]) != diff):
                    continue # its beautiful so go check for the next value of i

                else: # else if its not beautiful
                    is_Beautiful = False
                    break # break immediately, warna aage k element true ho skte hai

            # skipping the cuurent element in subset
            skip = find_subsets(nums, diff, index + 1, mask)

            # taking the current element into the subset
            if is_Beautiful:
                take = find_subsets(nums, diff, index+1,  mask + (1 << index))
            else:
                take = 0 # beautiful ni to isko ni lenge

            return take + skip

                
        res = find_subsets(nums, k, 0, 0)

        return res

# Driver's Code  
Result = Solution()     
subsets = Result.beautifulSubsets([2, 4, 6], 2) # output: 4
print(subsets)

subsets = Result.beautifulSubsets([10,4,5,7,2,1], 3) # ouput: 23
print(subsets)

"""
Detailed Explanation of each line of code:

Let's break down the code step by step to understand its functionality and the specific line you're curious about.

### Explanation of the Code

#### Class Definition
```python
class Solution:
    def beautifulSubsets(self, nums, k):
        return self._count_beautiful_subsets(nums, k, 0, 0)
```
- `beautifulSubsets` is the main method that initializes the recursive process.
- It calls `_count_beautiful_subsets` with the initial parameters: `nums`, `k`, starting index `0`, and starting mask `0`.

#### Recursive Helper Method
```python
def _count_beautiful_subsets(self, nums, difference, index, mask):
```
- This method counts the number of beautiful subsets recursively.
- Parameters:
  - `nums`: The list of integers.
  - `difference`: The integer `k` representing the required difference.
  - `index`: The current index in `nums` being considered.
  - `mask`: An integer where each bit represents whether a corresponding element in `nums` is included in the current subset.

#### Base Case
```python
if index == len(nums):
    return 1 if mask > 0 else 0
```
- If we have processed all elements (`index` is equal to the length of `nums`):
  - Return `1` if the current subset (represented by `mask`) is non-empty (i.e., `mask > 0`).
  - Return `0` if the current subset is empty.

#### Check if the Current Subset is Beautiful
```python
is_beautiful = True

for j in range(index):
    if ((1 << j) & mask) == 0 or \
       abs(nums[j] - nums[index]) != difference:
        continue
    else:
        is_beautiful = False
        break
```
- `is_beautiful` is initialized to `True`.
- The loop checks if adding `nums[index]` to the subset (represented by `mask`) keeps the subset beautiful.
- For each element `nums[j]` before `index`:
  - `((1 << j) & mask) == 0` checks if `nums[j]` is not in the current subset. 
    - `1 << j` creates a mask with the `j`-th bit set.
    - `& mask` checks if this bit is also set in the current `mask`.
    - If the result is `0`, `nums[j]` is not included in the subset.
  - `abs(nums[j] - nums[index]) != difference` checks if the absolute difference between `nums[j]` and `nums[index]` is not equal to `k`.
  - If both conditions are true, the loop continues; otherwise, `is_beautiful` is set to `False` and the loop breaks.

#### Recursive Calculation
```python
skip = self._count_beautiful_subsets(nums, difference, index + 1, mask)
take = (
    self._count_beautiful_subsets(
        nums, difference, index + 1, mask + (1 << index)
    )
    if is_beautiful
    else 0
)
```
- `skip`: Recursively calculates the count of beautiful subsets excluding `nums[index]`.
- `take`: Recursively calculates the count of beautiful subsets including `nums[index]`, only if `is_beautiful` is `True`.
  - `mask + (1 << index)` adds `nums[index]` to the subset by setting the `index`-th bit in `mask`.

#### Return the Result
```python
return skip + take
```
- Returns the sum of the counts of beautiful subsets excluding and including `nums[index]`.

### The Specific Line
```python
if ((1 << j) & mask) == 0 or \
   abs(nums[j] - nums[index]) != difference:
```
This line is crucial for checking if the current subset remains beautiful when `nums[index]` is added:

- `((1 << j) & mask) == 0`:
  - `1 << j` creates a binary number with only the `j`-th bit set.
  - `& mask` checks if the `j`-th bit in `mask` is also set (i.e., if `nums[j]` is included in the current subset).
  - `== 0` means `nums[j]` is not included in the current subset.
- `abs(nums[j] - nums[index]) != difference`:
  - Checks if the absolute difference between `nums[j]` and `nums[index]` is not equal to `k`.

The line ensures that either `nums[j]` is not in the subset or the difference condition is not violated, allowing the subset to be considered beautiful. If both conditions are false, the subset would not be beautiful, and `is_beautiful` is set to `False`.
"""