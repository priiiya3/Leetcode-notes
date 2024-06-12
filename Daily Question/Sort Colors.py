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

        