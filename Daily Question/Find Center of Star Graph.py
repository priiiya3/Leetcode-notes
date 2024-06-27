# Day 31

# Leetcode Notes 1791: Find Center of Star Graph

# Problem Statement:
"""
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 

Example 1:
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

Example 2:
Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1

Constraints:
3 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
The given edges represent a valid star graph.
"""

# Approach:
"""
This is A very easy question, 2D array diya hai nx2 sixe ka. apne ko bas common edge btani hai tree ki. yani wo edge jisse baaki saari edges connected hai

Simple hai bhai, since wo centre edge hai and saari edges usse connected hai, 
ham edges array k first two elements consider krengge.

Bas we will simply check ki kya first element ke u, v me se koi ek bhi second element odf edges me present hai. 
agar u present hai edges[1] me yani wo repeated hai yani wahi centre edge hai else its v.
"""

# Solution:
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        u_first, v_first = edges[0] # take the u, v edges of first element

        # check if u_first of first element (i.e, edges[0]) is present in edges[1] (that is second element of edges)
        # if it is return u_first since its repeated hence this must me centre /common egde else if its not then v_first
        # must be the repeating one

        return u_first if u_first in edges[1] else v_first # yha edges[1] hi ni 1 se n k beech kisi bhi edge par check kr skte hai, u_first, v_first me se jo common hai, wo saare me present hoga.
    
# Driver's Code:
Result = Solution()

# Test Case 1:
testcase1 = Result.findCenter([[1,2],[2,3],[4,2]])
print(testcase1) # expected 2

# Test Case 2:
testcase2 = Result.findCenter([[1,2],[5,1],[1,3],[1,4]])
print(testcase2) # expected 1
