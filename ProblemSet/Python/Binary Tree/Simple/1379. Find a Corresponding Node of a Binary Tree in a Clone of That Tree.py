# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original: # 遍历到叶子结点之下的空结点，直接返回，从而可以回到叶子结点
            return
        if original == target: # 判断当前结点是否为目标结点
            return cloned
        left = self.getTargetCopy(original.left, cloned.left, target) # 遍历左子树
        right = self.getTargetCopy(original.right, cloned.right, target) # 遍历右子树
        return left or right # 返回左子树或者右子树，如果目标结点出现了，返回会是一个cloned，如果未出现则为None
