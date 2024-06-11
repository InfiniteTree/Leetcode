# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0 # count the appearence time of the cur.val
        self.max_count = 0 # count the appearence time of the mode
        self.mode = []
        self.pre = None 

    def traversal(self, cur: Optional[TreeNode]) -> None:
        if not cur:
            return
        self.traversal(cur.left)
        if not self.pre:
            self.count = 1
        elif self.pre and self.pre.val == cur.val:
            self.count += 1
        else:
            self.count = 1
        if self.count == self.max_count:
            self.mode.append(cur.val)
        elif self.count > self.max_count:
            self.max_count = self.count
            self.mode = [cur.val]
            ###self.mode = []
            ###self.mode.append(cur.val)
        self.pre = cur
        self.traversal(cur.right)
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root)
        return self.mode

