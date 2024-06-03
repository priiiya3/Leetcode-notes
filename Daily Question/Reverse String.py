# DAY 10
## Leetcoe Problem 344: Reverse String

"""
Problem:
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""

## Solution:

from typing import List


class Solution1:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Two pointer method
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        
            
# Solution 2:
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # recursive method
        def recur(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
            return recur(l-1, r+1)

# Driver's Code
Result1 = Solution1()
Result2 = Solution2()


# Test Case for solution 1:
str1 = ["h","e","l","l","o"]
testcase1 = Result1.reverseString(str1)
print(str1) # expected: ["o","l","l","e","h"]

# Test Case for solution 2:
str2 = ["H","a","n","n","a","h"]
testcase1 = Result2.reverseString(str2)
print(str2) # expected: ["h","a","n","n","a","H"]
            