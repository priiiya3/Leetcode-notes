# Day 30

# Leetcode Problem 1382: Balance a Binary Search Tree


# Problem Statement:
"""
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 
Example 1:
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.


Example 2:
Input: root = [2,1,3]
Output: [2,1,3]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 105
"""

# Approach
"""
Approach bht easy hai. Apne ko bas aise karke binary tree ko arrange krna ho ki wo balaned binary tree ban jaye.

Balanced Binary tree wo hota hai jisme depth of the two subtrees of every node never differs by more than 1.

To isko solve karne k liye apan kya karenge ki:

step1: pahle saare nodes ko traverse krke ek array me save kr lenge.

step2: phir ham recursive call krke har particular root ko uske left aur right node se jodenge.

ham start array k mid element se krenge phir, mid element ko uske left and right child se attach krke 
ohir ham uske left side me move krenge aur wha k mid element k left and right child ko leke ek new Tree Node bnayenge, phir isko phle wale tree se attach kr denge.
Aise krke ham dheere dheere poora tree bna lenge. 
###### Read leetcode solutio  and see slideshow to understand better #####
"""


# Solution:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorderRec(root, inorder):
            """fucntion to perform inorder traversal and store order in array"""
            if not root: return

            inorderRec(root.left, inorder)
            inorder.append(root.val)
            inorderRec(root.right, inorder)

        def createTree(inorder, start, end):
            if start > end: return # Base case

            # find the middle element
            mid = start + (end - start)//2

            # recursiverly contruct left and right subtree
            leftSide = createTree(inorder, start, mid-1)
            rightSide = createTree(inorder, mid+1, end)

            # create new node as middle element and attach the subtree
            node = TreeNode(inorder[mid], leftSide, rightSide)

            return node
        
# Driver's Code:

Result = Solution()

# # Test Case 1
# testcase1 = Result.balanceBST(root =[1,null,2,null,3,null,4,null,null])
# print(testcase1)