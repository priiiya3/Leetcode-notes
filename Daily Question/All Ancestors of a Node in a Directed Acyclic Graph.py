# Day 33

# Leetcode Problem 33: All Ancestors of a Node in a Directed Acyclic Graph

# Problem Statement:
"""
You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).
You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.
Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.
A node u is an ancestor of another node v if u can reach v via a set of edges.

 

Example 1:
Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
Explanation:
The above diagram represents the input graph.
- Nodes 0, 1, and 2 do not have any ancestors.
- Node 3 has two ancestors 0 and 1.
- Node 4 has two ancestors 0 and 2.
- Node 5 has three ancestors 0, 1, and 3.
- Node 6 has five ancestors 0, 1, 2, 3, and 4.
- Node 7 has four ancestors 0, 1, 2, and 3.

Example 2:
Input: n = 5, edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Output: [[],[0],[0,1],[0,1,2],[0,1,2,3]]
Explanation:
The above diagram represents the input graph.
- Node 0 does not have any ancestor.
- Node 1 has one ancestor 0.
- Node 2 has two ancestors 0 and 1.
- Node 3 has three ancestors 0, 1, and 2.
- Node 4 has four ancestors 0, 1, 2, and 3.
 

Constraints:

1 <= n <= 1000
0 <= edges.length <= min(2000, n * (n - 1) / 2)
edges[i].length == 2
0 <= fromi, toi <= n - 1
fromi != toi
There are no duplicate edges.
The graph is directed and acyclic.
"""

# Approach:
"""
Hame har nodes k ancesstors return karne hai. Jinke ancesstor in unke jagah hm [] return krenge.

Idea simple hai ham DFS use krenge to find out har node ka parents. But instead of parent se uska child find krne k,
Ham child k through uska parent khojenge. Isse easy padega. Consequently, nodes reachable from a given node in the reversed graph were its ancestors in the original graph

To find the descendants of a node v, we start a depth-first traversal from v in the reversed graph, using a visited set to track nodes. 
After the traversal, we collect all nodes in visited (except v) in a list, representing the ancestors of v in the original graph. 
Performing this traversal for each node provides the required ancestors for all nodes.
"""

# Solution:
from typing import List
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        def dfs(node, adj_list, visited):
            
            # add current node to visited set
            visited.add(node)

            # traverse the neighbour node of current node
            for nei in adj_list[node]:
                if nei not in visited:
                    dfs(nei, adj_list, visited)
        

        # main function code

        # create adjency list
        adj_list = [[] for i in range(n)]
        # connect nodes in adjency list
        for frm, to in edges:
            adj_list[to].append(frm)

        # create variables
        all_ancesstors = [] # to store ancesstors of all the nodes

        # traverse all nodes from 1 to n
        for i in range(n):
            seen = set()
            curr_ancesstors = [] # ancesstors of current node
            # call dfs to find parents of current node
            dfs(i, adj_list, seen)

            for node in range(n):
                if node == i: # ignore current node
                    continue
                if node in seen: # if node in seen that means its their ancesstor
                    curr_ancesstors.append(node)
            # add list of ancesstors of current node to final ancesstor list
            all_ancesstors.append(curr_ancesstors)

        return all_ancesstors


# Driver's Code
Result = Solution()

# Test Case 1:
testcase1 = Result.getAncestors(n=8, edges=[[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]])
print(testcase1) # expected: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]

# Test Case 2:
testcase2 = Result.getAncestors(n=5, edges=[[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
print(testcase2) # expected: [[],[0],[0,1],[0,1,2],[0,1,2,3]]   

