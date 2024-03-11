# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetricTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case
        if p is None or q is None:
            return p is q
        # Recursion
        return p.val == q.val and self.isSymmetricTree(p.left, q.right) and self.isSymmetricTree(q.left, p.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricTree(root.left, root.right)
        