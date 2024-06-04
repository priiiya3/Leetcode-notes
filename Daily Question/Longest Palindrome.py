# Day 11
# Leetcode Problem 409: Longest Palindrome

# Problem Statement:
"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""

## AQpproach:
"""
palindrome me hmesha middle wale character ko chhod k baki sb ka repetition even times hoga. 
Hence simple sa logic hai, apan counter me add krenge jo jo elment even times repeated hai. 
aur ek character wo add krenge jiska cnt odd hai. because middle element ka count odd ho skta h (like 1, 3, 5).

also apan ek flag maintain krenge taki apan ko pta rhe ki odd element hai mid me ya ni.

"""

# Solution:
from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # dictionary to store frequency of each character
        freq = Counter(s)
        
        # variables to store count and flag for checking if an element is odd
        odd_freq, res = False, 0

        for counts in freq.values():
            if counts % 2 == 0:
                res += counts
            else:
                res += counts - 1
                odd_freq = True
        return res + 1 if odd_freq else res 
    
Result = Solution()

# Test Case 1
testcase1 = Result.longestPalindrome("abccccdd")
print(testcase1) # expected: 7

# Test Case 2
testcase2 = Result.longestPalindrome("a")
print(testcase2) # expected: 1