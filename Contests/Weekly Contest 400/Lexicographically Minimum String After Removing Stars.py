# Problem 3170: Lexicographically Minimum String After Removing Stars

"""
You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the 
lexicographically smallest
 resulting string after removing all '*' characters.

 

Example 1:

Input: s = "aaba*"

Output: "aab"

Explanation:

We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

Example 2:

Input: s = "abc"

Output: "abc"

Explanation:

There is no '*' in the string.

 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters and '*'.
The input is generated such that it is possible to delete all '*' characters.
"""

# Approach:
"""
isme apne ko jo first '*' mile uske left me jo nearest and smalled char hai usko hatana hai. yani agar we have multiple
lexicographically smallest char present in the left of '*', remove the one with highest index value, because its nearest to '*'.

Keeping the index thing in mind, I though of using min-heap. Since using min-heap, we will easily know which is the smallest so far.
Also, we will store indices in -negative in min heap, so the index with highest value becomes least, and thus takes the position of parent node in min-heap
So that we can pop smallest possible and nearest indexed char whenever we encounter '*'.
"""

## Solution:
import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        """heap in mpython is min-heap by default"""
        heap = []
        for i, ch in enumerate(s):
            if ch == '*':
                if heap:
                    heapq.heappop(heap)
            else:
                heapq.heappush(heap, (ch, -i))
                # we are using -i here, because apne ko * se nearest (& smallest) element remove krna hai. 
				# and index se apan sjh skte hai ki nearest char wahi hai jiska index higher hai.

				# Explaining More:
                # suppose we have a string 'aaba*', then min heap for this will be: [('a', -3), ('a', -1), ('b', -2), ('a', 0)]
                # here heap will see that among a and b, a is smaller, then it will check indices of all a's and 
                # among [('a', -3), ('a', -1), ('a', 0)], 3 is neared to '*', so that will be popped, then -1, then 0, then b will come next.
				# isliye apan -3 use kr rhe, qki python by default min-heap k tarah kaam krta hai, and 3 ko -3 me badalne pr apne ko easy hoga min index khojne me

        ans = [''] * len(s)

        while heap:
            ch, i = heapq.heappop(heap)
            ans[-i] = ch  
                
        return ''.join(ans)
                    

Ret = Solution()

# Test Case 1:
testcase1 = Ret.clearStars('aaba*')
print(testcase1) # expected: 'aab'

# Test Case 2:
testcase2 = Ret.clearStars('abc')
print(testcase2) # expected: 'abc'

# Test Case 3:
testcase1 = Ret.clearStars('de*')
print(testcase1) # expected: 'e'