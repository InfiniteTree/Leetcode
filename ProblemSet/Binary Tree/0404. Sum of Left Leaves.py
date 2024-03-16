# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeftLeaves(self, cur: Optional[TreeNode]) -> int:
        # Base Case
        if not cur: # None node
            return 0
        if  not cur.left and not cur.right: # leaves node
            return 0
        
        # Recursion
        leftNum = 0
        if cur.left and not cur.left.left and not cur.left.right:
            leftNum = cur.left.val
        return leftNum + self.getLeftLeaves(cur.right) + self.getLeftLeaves(cur.left)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:    
        return self.getLeftLeaves(root)
