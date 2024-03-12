# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(cur: Optional[TreeNode], target, path) -> bool:
            # Base Case
            if not cur: 
                return False
            if not cur.left and not cur.right:
                if path[0] == target:
                    return True
            # Recursion
            if cur.left:
                path[0] += cur.left.val
                if dfs(cur.left, target, path):
                    return True
                path[0] -= cur.left.val
            if cur.right:
                path[0] += cur.right.val
                if dfs(cur.right, target, path):
                    return True
                path[0] -= cur.right.val
            return False
        
        if not root:
            return False
        path = [root.val]
        return dfs(root, targetSum, path)
