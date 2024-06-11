# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, cur:Optional[TreeNode], preSum: int) -> int:
        if not cur:
            return 0
        
        curSum = preSum * 10 + cur.val
        if cur and not cur.left and not cur.right:
            return curSum
        left = self.traversal(cur.left, curSum)
        right = self.traversal(cur.right, curSum)
        return left + right
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        initSum = 0
        return self.traversal(root, initSum)
        