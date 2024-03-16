# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                # loop length (l) = (fast - slow) - 1 = slow - 1
                # start loop index = list length - loop length: idx = len(list) - slow + 1
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow
        return None
        