# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, cur: Optional[TreeNode], path: List, res: List[string] ) -> List[str]:
        path.append(cur.val)
        if not cur.left and not cur.right:
            res.append('->'.join(map(str, path)))
            return
        if cur.left:
            self.traversal(cur.left, path, res)
            path.pop()
        if cur.right:
            self.traversal(cur.right, path, res)
            path.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path, res = [], []
        self.traversal(root, path, res)
        return res
