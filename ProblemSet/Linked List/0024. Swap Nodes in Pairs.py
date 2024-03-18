# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next and cur.next.next:
            nxt = cur.next
            nxt1 = cur.next.next.next
            cur.next = cur.next.next
            cur.next.next = nxt
            nxt.next = nxt1 # cur.next.next.next = nxt1 
            cur = cur.next.next
        return dummy.next
        