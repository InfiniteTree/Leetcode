# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(cur: Optional[TreeNode], target, path, res) -> List[List[int]]:
            # Base Case:
            if not cur:
                return
            path.append(cur.val)
            if not cur.left and not cur.right:
                if sum(path) == target:
                    res.append(path.copy())
            dfs(cur.left, target, path, res)
            dfs(cur.right, target, path, res)
            path.pop()
            #return

        if not root:
            return []
        res, path = [], []
        dfs(root, targetSum, path, res)
        return res