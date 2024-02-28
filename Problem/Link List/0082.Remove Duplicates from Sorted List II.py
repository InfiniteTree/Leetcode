# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next and cur.next.next:
            temp = cur.next.val
            if cur.next.next.val == temp:
                while cur.next and cur.next.val == temp:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
        