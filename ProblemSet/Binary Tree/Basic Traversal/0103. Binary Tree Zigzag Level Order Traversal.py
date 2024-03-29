# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ret = []
        q = deque([root])
        even = False
        while q:
            one_level = []
            for _ in range(len(q)):
                node = q.popleft()
                one_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if even:
                one_level = one_level[::-1]
            even = not even
            ret.append(one_level)
        return ret       
        