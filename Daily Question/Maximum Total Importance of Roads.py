# Day 32

# Leetcode Problem 2285: Maximum Total Importance of Roads

# Problem Statement:
"""
You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the values optimally.

 

Example 1:
Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output: 43
Explanation: The figure above shows the country and the assigned values of [2,4,5,3,1].
- The road (0,1) has an importance of 2 + 4 = 6.
- The road (1,2) has an importance of 4 + 5 = 9.
- The road (2,3) has an importance of 5 + 3 = 8.
- The road (0,2) has an importance of 2 + 5 = 7.
- The road (1,3) has an importance of 4 + 3 = 7.
- The road (2,4) has an importance of 5 + 1 = 6.
The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
It can be shown that we cannot obtain a greater total importance than 43.


Example 2:
Input: n = 5, roads = [[0,3],[2,4],[1,3]]
Output: 20
Explanation: The figure above shows the country and the assigned values of [4,3,2,5,1].
- The road (0,3) has an importance of 4 + 5 = 9.
- The road (2,4) has an importance of 2 + 1 = 3.
- The road (1,3) has an importance of 3 + 5 = 8.
The total importance of all roads is 9 + 3 + 8 = 20.
It can be shown that we cannot obtain a greater total importance than 20.
 

Constraints:

2 <= n <= 5 * 104
1 <= roads.length <= 5 * 104
roads[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
There are no duplicate roads.
"""

# Approach:
"""
Apne ko nodes ko value assign karni hai in such a manner ki unka total possible sum maximum ho. 
Total possible sum bole to saare tarike se nodes ko connect krne ka sum.

Bahot simple approach, since jis node ki degree jyada hogi wo jyada baar travel kr rhe honge ham to that means 
highest degree wale ko agar ham biggest value assign krenge to sum maximize hoga.

Hence apna solution 3 step me hoga:

Step 1: Ham har node ki degree calculate krenge
Step 2: degrees ko ascending order me arrange krenge
Step 3: degree me start to end traverse karenge and since ye ASC order me hai start element min degree wala hai, to uski val 1 rakkhenge 
    and total banyenge total += degree[i] * value (where value = 1 and i = 0)
    Phir jaise jaise i increment hoga, degree badhegi to ham value ko bhi increment krenge by 1. (i.e, value +=1)

"""

# Solution:
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        # step 1: count the degree of each node
        degree = [0] * n
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1

        # step 2: sort degree in Ascending order
        degree.sort()

        # step 3: calculate total sum
        max_total_sum = 0
        value = 1
        for deg in degree:
            max_total_sum += value * deg 
            value += 1 # increment value by 1 for next node with higher degree

        return max_total_sum
    
# Driver's Code:
Result = Solution()

# Test Case 1:
testcase1 = Result.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])
print(testcase1) # expected: 43

# Test Case 2:
testcase2 = Result.maximumImportance(5, [[0,3],[2,4],[1,3]])
print(testcase2) # expected: 20