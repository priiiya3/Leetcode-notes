# Day 18
# Leetcode Problem 74: Sort Colors

# Problem Statement
"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

# Approach:
"""
Iss problem ko solve karne ka best approach hai Three pointers use karna. 
Isko Dutch National Flag Problem bhi bolte hai.

Ham basically isme 3 pointers lete hai: start, mid, end. Start & mid 0th index ko point krenge and end pointer last index ko.
Ab inme mid pointers har baar mobe krega jabki start and end pointers special conditions milne pr hi move krenge.

yani ki array me mid start se chalna shuru krega, usko agar pehla element 0 mila to wo start k position pr present element se usko swap krega aur
ek step aage badh jayega. and start bhi mid k phle wali position me aa jayega. 
Similarly agar mid ko 2 mila to wo end pointer se usko swap krega, adn end pointer ek kadam left me move kr jayega.
(iss case me ham mid ko move ni krenge qki hme sure ni ki end pointer se jo value swap ki hai wo 1 hai ya 0 ya 2).


So mainly end me ye algorithm use karne se... start pointer k left k saare element 0 (zero) hone
and end pointer k right k saare elements 2 (two) honge.
"""

# Solution
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, mid, end = 0, 0, len(nums)-1

        while mid < len(nums) and end >= mid:
            if nums[mid] == 0:
                nums[start], nums[mid] = nums[mid], nums[start] # swap the elements
                start += 1 # move start pointer one step to right
                mid += 1 # move mid pointer one step to right 
            elif nums[mid] == 2:
                nums[end], nums[mid] = nums[mid], nums[end] # swap the elements
                end -= 1 # move end pointer one step to left    
            else: # if nums[mid] == 1
                mid += 1

        return nums
    
# Driver's Code
Result = Solution()

# Test Case 1:
testcase1 = Result.sortColors([2,0,2,1,1,0])
print(testcase1) # expected: [0, 0, 1, 1, 2, 2]

# Test Case 2:
testcase2 = Result.sortColors([2, 0, 1]) 
print(testcase2) # expected: [0, 1, 2]




"""
#### Approach 1: FROM HINTS => 
count the number of occurences of 0, 1 and 2 and add them in the new array and return
TC: O(N) , SC: O(N)

CODE:
```
# variables to store count of zero, one and two
        zero, one, two = 0, 0, 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            elif nums[i] == 1:
                one += 1
            else:
                two += 1
        
        for i in range(len(nums)):
            if zero != 0:
                nums[i] = 0
                zero -= 1
                
            elif one != 0:
                nums[i] = 1
                one -= 1
                
            else:
                nums[i] = 2
                two -= 1
```

---------------------------------------------------------------------------------------------------
#### Approach 2: Using Selection Sort =>
 TC: O(N), SC: O(1)

```

        
        for i in range(len(nums)):
            mini = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[mini]:
                    mini = j
                    
            # swap current and minimum element
            nums[i], nums[mini] = nums[mini], nums[i]
            
        return nums
                
        
```


----------------------------------------------------------------------------------------------------
#### Approach 3: Dutch National Flag: (One Pass)

code:
```
def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag problem solution.
        """
        
        left, right, mover = 0, len(nums) - 1, 0
        
        while mover <= right:
                
            if nums[mover] == 0:
                nums[mover], nums[left] = nums[left], nums[mover]
                left  += 1
                mover += 1
                # yha dono ko +1 kar rhe qki mover k place pe
            # pakka 1 hi aya hoga after swap, qki apan isi baat ka to
            # code me dhyan de rhe ki mover k left me 2 na ho sirf 0 & 1 ho
                    
            elif nums[mover] == 2:
                nums[mover], nums[right] = nums[right], nums[mover]
                right -= 1
                # yha mover to +1 ni kar rhe qki maybe swap jo huwe h
                # do numbers (mover & right) dono ki value 2.
            else:
                mover += 1
```


Best approach So far.
TC: O(n), SC: O(1)


---------------------------------------
-----------------------------------------------------




"""