# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, q: Optional[TreeNode], p: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        leftside = self.isSameTree(p.left, q.left)
        rightside = self.isSameTree(p.right, q.right)
        return p.val == q.val if leftside and rightside else False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)