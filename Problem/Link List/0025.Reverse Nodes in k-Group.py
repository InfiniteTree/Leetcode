# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        n = 0 # the number of the nodes
        while cur:
            n += 1
            cur = cur.next
  
        dummy = ListNode(next=head)
        p0 = dummy
        loop_n = n // k # the loop time
        while loop_n > 0:
            pre = None
            cur = p0.next
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt               
            
            # Update the pre p0 node of the kth reversed sublink
            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
            loop_n -= 1

        return dummy.next
        