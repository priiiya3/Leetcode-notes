# DAY 11
## Leetcoe Problem 2486: Append Characters to String to Make Subsequence

## Problem Statement:
"""
You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

Example 1:

Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
Example 2:

Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").
Example 3:

Input: s = "z", t = "abcde"
Output: 5
Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s ("zabcde").
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.
 

Constraints:

1 <= s.length, t.length <= 105
s and t consist only of lowercase English letters.
"""

## Approach:
"""
approach is very straight forward, very easy question. Apne ko bas dekhna hai t string k kon kon se character
already s string me present hai. Hence to do this we will do normal index based comaprison. 
in the end, s string k jitne character t string me sequentially mile, unke count ko t string 
k length se subtract krdo and you will get the number of charc we need to add in string s to make t, a subseques of s.

I have usex two pointers to compare subsequent elments in s and t string
"""

## Solution:
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        
        cnt, j = 0, 0
        maxlen = 0
        for i in range(len(s)):
            # print(i, j)
            if j < len(t) and s[i] == t[j]:
                j += 1
                cnt += 1

            maxlen = max(maxlen, cnt)

        return len(t) - maxlen
    
# Driver's Code
Result = Solution()

# Test Case 1: 
testcase1 = Result.appendCharacters(s = "coaching", t = "coding")
print(testcase1) # expected:4 ( Append the characters "ding" to the end of s so that s = "coachingding".)

# Test Case 2: 
testcase2 = Result.appendCharacters(s = "abcde", t = "a")
print(testcase2) # expected: 0 (t is already a subsequence of s ("abcde").)

# Test Case 3: 
testcase3 = Result.appendCharacters(s = "z", t = "abcde")
print(testcase3) # expected: 5 (Append the characters "abcde" to the end of s so that s = "zabcde".)