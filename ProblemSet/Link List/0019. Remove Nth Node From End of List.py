# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Method 1
        dummy = ListNode(next=head)
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
        
        p0 = dummy
        for _ in range(cnt-n):
            p0 = p0.next
        p0.next = p0.next.next

        return dummy.next
    
        # Method two 
        # Use ptr start walking from the start
        # First Let the right ptr to point to the nth node
        # Then let the left ptr to right ptr to walk together
        # When the right ptr reach the end, the left prt exaclty points to the nth node from the end
        