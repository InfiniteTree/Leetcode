# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # Method 1. From top to the bottom
        '''
        # maxDif = -inf
        maxDif = [float("-inf")]
        ancts = []
        def traversal(cur: Optional[TreeNode], mini: int, maxi: int) -> None: 
            if not cur:
                maxDif[0] = max(maxDif[0], maxi-mini) # Optimization
                return
            mini = min(mini, cur.val)
            maxi = max(maxi, cur.val)
            # nonlocal maxDif
            # maxDif = max(maxDif[0], abs(cur.val-mini), abs(maxi-cur.val))
            # maxDif[0] = max(maxDif[0], abs(cur.val-mini), abs(maxi-cur.val))
            traversal(cur.left, mini, maxi)
            traversal(cur.right, mini, maxi)
            return
        traversal(root, root.val, root.val)
        return maxDif[0]
        #return maxDif
        '''

        # Method 2. From bottom to top
        ans = 0
        def dfs(node: Optional[TreeNode]) -> (int, int):
            if node is None:
                return inf, -inf
            # mn = mx = node.val
            l_mn, l_mx = dfs(node.left)
            r_mn, r_mx = dfs(node.right)
            mn = min(node.val, l_mn, r_mn)
            mx = max(node.val, l_mx, r_mx)
            nonlocal ans
            ans = max(ans, node.val - mn, mx - node.val)
            return mn, mx
        dfs(root)
        return ans
