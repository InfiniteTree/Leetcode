# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return
        #mid = (left+right)//2
        mid = left + (right - left)//2
        root = TreeNode(nums[mid])
        root.left = self.traversal(nums, left, mid-1)
        root.right = self.traversal(nums, mid+1, right)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.traversal(nums, 0, len(nums)-1)
        