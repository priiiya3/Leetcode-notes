# Day 10
# Leetcode Problem 3110: Score of a String

# Problem Statement:
"""
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.

 

Example 1:

Input: s = "hello"

Output: 13

Explanation:

The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

Example 2:

Input: s = "zaz"

Output: 50

Explanation:

The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.

 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
"""

## Approach
"""
The question is easy level, very simple approach used. just take a while loop from 1 to len(string) and a varible to store sum.
Inside loop perform sum = sum + abs( ascii_value_of(s[i-1] - ascii_value_of(s[i])))
return sum in the end.
Time Complexity: O(N), Space Complexity: O(1)
"""

## Solution:
class Solution:
    def scoreOfString(self, s: str) -> int:
        
        Sum = 0
        for i in range(1, len(s)):
            Sum += abs(ord(s[i-1]) - ord(s[i]))

        return Sum
    
# Driver's Code:
Result = Solution()

# TestCase 1 
testcase1 = Result.scoreOfString("hello")
print(testcase1) # expected: 13

# TestCase 2
testcase2 = Result.scoreOfString("zaz")
print(testcase2) # expected: 50