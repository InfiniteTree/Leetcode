# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def robTree(self, cur: Optional[TreeNode]) -> list:
        if cur == None: # the current node is none
            return [0, 0]
        # Dp[0] indicates not to rob while Dp[1] indicates to rob 
        leftDp = self.robTree(cur.left)
        rightDp = self.robTree(cur.right)
        # Do not rob the cur Node, whichi indicates whether to rob or not to rob its children
        val0 = max(leftDp[0], leftDp[1]) +  max(rightDp[0], rightDp[1])
        # rob the cur node, which inplies not to rob its children
        val1 = cur.val + leftDp[0] + rightDp[0] 
        return [val0, val1]

    def rob(self, root: Optional[TreeNode]) -> int:
        result = self.robTree(root)
        return max(result[0], result[1])
        #return max(self.robTree(root))
