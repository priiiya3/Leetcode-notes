# Day 7
# Leetcode Problem 1208: Get Equal Substrings Within Budget

# Problem Statement:
"""
You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.

 

Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.
Example 2:

1 <= s.length <= 105
t.length == s.length
0 <= maxCost <= 106
s and t consist of only lowercase English letters.
"""

## Approach:

"""
Method1: Brute Force
First I though of brute force method so like we start from i = 0 and count cost till cost < maxCost for each array element, 
then we increate i by one, start again counting cost from i=1'th element till cost < maxCost
then again for i = 3. And we keep storing the maxlength we converted and return that atlast. 

This approach gave TLE. Time Complexity: O(N*N)

Then I tried window sliding method. So you use two points slow and fast, both starts from index = 0.
we keep adding element to cost (by moving fast pointer) till cost <= maxCost thus "Expanding the Sliding Window".
when cost becomes: cost > maxCost we move the slow pointer till cost again becomes less than maxCost. Thus "Shrinking the Sliding Window".

"""

# Solution:
# Sliding Window Solution:
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        slow, fast = 0, len(s) - 1
        res, cost = 0, 0

        for fast in range(len(s)):
            cost += abs(ord(s[fast]) - ord(t[fast]))

            while cost > maxCost:
                cost -= abs(ord(s[slow]) - ord(t[slow]))
                slow += 1

            res  = max(res, (fast - slow) + 1)

        return res
    
# Driver's Code
result = Solution()

# TestCase 1
testcase1 = result.equalSubstring("abcd", "bcdf", 3)
print(testcase1) # Expected: 3

testcase1 = result.equalSubstring("a", "z", 0)
print(testcase1) # Expected: 0

testcase1 = result.equalSubstring("krrgw", "zjxss", 19)
print(testcase1) # Expected: 2

"""##Brute Force Solution:
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        cnt = 0
        i = 0
        ans = 0
        while i < len(s):
            diff = abs(ord(s[i]) - ord(t[i]))
            res = 0
            if diff <= maxCost:
                j= i
                cnt = maxCost
                while j < len(s):
                    nums = abs(ord(s[j]) - ord(t[j]))
                    if nums <= cnt:
                        cnt -= nums
                        res += 1
                    else:
                        break
                    j += 1
            i += 1
            print(ans, res)
            ans = max(ans, res)

        return ans

"""