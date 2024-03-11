# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, node):
        # Base case
        if node is None:
            return 0
        # Recursion
        l_height = self.getHeight(node.left)
        if l_height == -1:
            return -1
        r_height = self.getHeight(node.right)
        if r_height == -1:
            return -1
        if abs(r_height-l_height) > 1:
            return -1
        return max(l_height, r_height) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root) != -1
