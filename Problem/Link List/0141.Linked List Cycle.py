# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next: # use fast because fast.next.next is used in the code below and fast.next need to exist
            slow = slow.next # slow:+1
            fast = fast.next.next # fast: +2
            if fast == slow:
                return True
        return False
        