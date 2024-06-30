# Day 34

# Leetcode Problem 1579: Remove Max Number of Edges to Keep Graph Fully Traversable

# Problem Statement:
"""
Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

 

Constraints:

1 <= n <= 105
1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
edges[i].length == 3
1 <= typei <= 3
1 <= ui < vi <= n
All tuples (typei, ui, vi) are distinct.

"""

# Approach:

"""
Since we need to remove the extra repetetive adges. 
Ham simply phle jo common egde has alice and bob k liye wo connect krenge phir ham 2 cases lenge yha se:
case 1: ALICE: isme ham root node me further alice ki nodes ko connect krenge, aur jo nodes hme phle se connected milengi root me unko res += 1 krke cnt kr lenge
        qki yhi wo extra repetetive edges hai ince case of alice
case 2: BOB: isme bhi ham phir se start wala root node lenge jisme sirf commong edges connected thi and 
    connect krenge use bob ki accessible nodes. Jo nodes already connected ayengi yani wo repetetive hai, so we will again do res += 1

end me we will return this res if and only if alice and bob n-1 nodes ko traverse kr paa rhe. Agar nhi that means return -1 qki poora graph traverse karna possible nhi.

For solution algorithm, read my this leetcode article: https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/solutions/2833526/using-union-find-python-hindi-comments/

"""

# Solution:
from typing import List


class UnionFind():
    def __init__(self, size):
        self.root = list(range(size+1))
        self.rank = [0] * (size+1)
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)

        if rootX == rootY: # if they have same root
            # node x, and y are already connected
            return False
        elif self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        else:
            self.root[rootX] = rootY
            self.rank[rootY] += self.rank[rootX]
        return True
    
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # initialize the Union Find object
        uf = UnionFind(n)

        # variables to count number to nodes alice, bob can access and res to count common repetetive edges
        alice = bob = res = 0

        # First we will connect the nodes of tyep 3, that allows both alice and bob to traverse
        for type, u, v in edges:
            if type == 3:
                if uf.union(u, v): # # if both  u and v nodes have same root
                    # we increment both, bcz type:3 can be traverse by both
                    # alice and bob
                    alice += 1
                    bob += 1
                else: # if roots of u and v are not connected
                    res += 1 
        
        # apan copy bna lenge 3rd type edges ko connect krne k baad 
        # qki ab yha se hme dono k liye individually check krna hai ki saari
        # bachi nodes both alice & bob, dono ko reachable ko.. yani use node
        # par green and red dono lines ho.
        rootCopy = uf.root[::]

        # Case 2: Alice, i.e, type 1 wali edges
        for type, u, v in edges:
            if type == 1:
                if uf.union(u, v): # yani u and v k common root node hai.
                    alice += 1 # since ye node sirf alice travel kr skti hai, it has red line
                else: # 
                    res += 1
        
        
        # alice k traversal k baad ham root ki value phir se usse stage pr
        # re-set krenge jab sirf type : 3 connections hue thay
        uf.root = rootCopy

        # Case 3: BOB i.e, type 2
        for type, u, v in edges:
            if type == 2:
                if uf.union(u, v):
                    bob += 1
                else:
                    res += 1

        return res if alice == bob == n-1 else -1 # since agr alice ya bob ka cnt n-1 ni hoga that means aisi koi node hai jisko they are not able to traverse

# Driver's Code:
Result = Solution()

# Test Case 1:
testcase1 = Result.maxNumEdgesToRemove(n=4, edges=[[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]])
print(testcase1) # expected: 2

# Test Case 2:
testcase2 = Result.maxNumEdgesToRemove(n=4, edges=[[3,1,2],[3,2,3],[1,1,4],[2,1,4]])
print(testcase2) # expected: 0

# Test Case 3:
testcase3 = Result.maxNumEdgesToRemove(n=4, edges = [[3,2,3],[1,1,2],[2,3,4]])
print(testcase3) # expected: -1