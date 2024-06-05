# Day 12
# Leetcode Problem 1002: Find Common Characters

# Problem Statement:
"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""

## Approach
"""
Khud se ni hua to editorial se smjhna pada. 

Aproach simple ahi, do freqeuncy k map maintain krenge, ek jo har new word k liye update hota rhega, lets call it current_freq, 
and other will be the main/common one, jisse ham compare krenge curent se, lets call it common_freq.

ab bas apan phle common_freq me first word ko store krenge. fir words array k har ek word se macth karate jayenge.
"""

## Solution
from typing import List
from collections import Counter


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        res = [] # to store final common characters
        common_freq = Counter(words[0])

        for word in words[1:]:
            current_freq = Counter(word)

            for item, count in common_freq.items():
                common_freq[item] = min(count, current_freq[item])

        
        for ch, cnt in common_freq.items():
            for _ in range(cnt):
                res.append(ch)

        return res
    
# Driver's code
Result = Solution()

# Test Case 1:
testcase1 = Result.commonChars(["bella","label","roller"])
print(testcase1) # expected: ["e", "l", "l"]

# Test Case 2:
testcase2 = Result.commonChars(["cool","lock","cook"])
print(testcase2) # expected: ["c", "o"]