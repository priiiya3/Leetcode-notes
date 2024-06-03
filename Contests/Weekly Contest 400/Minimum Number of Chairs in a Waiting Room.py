# Problem:
"""
3168. Minimum Number of Chairs in a Waiting Room
Solved
Easy
Companies
Hint
You are given a string s. Simulate events at each second i:

If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
Return the minimum number of chairs needed so that a chair is available for every person who enters the waiting room given that it is initially empty.

 

Example 1:

Input: s = "EEEEEEE"

Output: 7

Explanation:

After each second, a person enters the waiting room and no person leaves it. Therefore, a minimum of 7 chairs is needed.
"""

## Approach:
# Very simple approach, if s[i] is 'E', increment counter & store max counter value so far in a seperate variable
# else if s[i] == 'L', then simply decrement counter. Return max value stored so far

## Solution:
class Solution:
    def minimumChairs(self, s: str) -> int:
        
        cnt, mx = 0, 0
        
        
        for ch in s:
            if ch == 'E':
                cnt += 1
                if cnt > mx:
                    mx = cnt
            elif ch == 'L':
                cnt -= 1
                
        return mx
# Driver's code
Ret = Solution()

# Test Case 1
testcase1 = Ret.minimumChairs('EEEEEEE')
print(testcase1) # expected: 7

# Test Case 2
testcase2 = Ret.minimumChairs('ELELEEL')
print(testcase2) # expected: 2