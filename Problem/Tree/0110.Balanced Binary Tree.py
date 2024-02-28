# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node):
            # Base case
            if node is None:
                return 0
            # Recursion
            l_height = getHeight(node.left)
            if l_height == -1:
                return -1
            r_height = getHeight(node.right)
            if r_height == -1 or abs(r_height-l_height) > 1:
                return -1
            return max(l_height, r_height) + 1
        return getHeight(root) != -1
