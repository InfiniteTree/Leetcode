# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 2024.03.13
class Solution:
    def __init__(self):
        self.pre = None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Base Case
        if not root:
            return True
        # Recursion
        left = self.isValidBST(root.left) # bool value
        if self.pre and self.pre.val >= root.val:
            return False
        self.pre = root
        right = self.isValidBST(root.right) # bool value
        return left and right
'''
# 2024.02.28
class Solution: 
    pre = -inf # Used in method 2
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ### Method 1: preorder traversal
        l, r = -inf, inf
        def check(node, left, right):
            if node is None:
                return True
            x = node.val
            return left < x < right and check(node.left, left, x) and check(node.right, x, right)
        return check(root, l, r)

        ### Method 2: inorder traversal

        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)

    ### Method 3: Postorder traversal
        def getRange(node):
            # Base case
            if node is None:
                # to ensure in the recursion step the if does not run if true
                return inf, -inf 
            
            # Recursion
            l_min, l_max = getRange(node.left)
            r_min, r_max = getRange(node.right)
            x = node.val
            if x<=l_max or x>=r_min:
                return -inf, inf
            return min(l_min, x), max(r_max, x)
        
        return getRange(root)[1] != inf
'''

