# DAY 17
## Leetcoe Problem 1122: Relative Sort Arrays

"""Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
 

Constraints:

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1."""

## Approach
"""
1. Approach Simple hai, apan na phle ek dictionary lenge jisme store krenge arr ke har array element ka count.
Taaki apne ko pta ho konsa element kitne baar aya hai.

2. ab apan map me phle store krenge arr2 k element, jo jo hme khojne hai arr1 me.

3. phir ham arr1 me ek ek karke dekhenge...agar arr1 ka current element map me present hai to result named array me current element ko map[arr1[i]] times 
store krenge. 
for example: arr2: [1, 2, 3], arr1: [1,2,2,1,3, 7, 8]
then map will be: map: {1: 2, 2: 2, 3: 1}. apan parallel me bache elements arr1 k, jo map me ni gye
unko left naam k array me daal denge.

ab ham arr2 me traverse krenge and dekhenge first element 1 hai aur uska count map me 2 hai, so result = [1, 1]
then arr2 ak second element hai 2, so result will become, result = [1, 1, 2, 2]
then last element 3 hai, so result will become, result = [1,2,2,2,3]

ab jo arr1 k remaining element hai, jo left array me hai unko result me add kr denge
"""

## Solution:
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        map = {} # to store count of all the elements present in the arr1
        extras, res = [], [] # left array to store extra elements of arr1 that are not present in arr2
        # adn res to return final resulting array

        for num in arr2:
            map[num] = 0

        for num in arr1:
            if num in map:
                map[num] += 1
            else:
                extras.append(num)

        for inx, val in map.items():
            res.append(inx*val)
        
        res.extend(extras)

        return res
