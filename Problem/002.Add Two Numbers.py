# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        '''
        # Method 1
        bounder = 10
        head = ListNode(0) # blank head node
        cur_node = head
        carry = 0
        while l1 and l2:
            # Calculate the digits sum of the current node
            dig_sum = l1.val + l2.val + carry
            if dig_sum >= bounder:
                carry = 1
                dig_sum -= bounder
            else:
                carry = 0

            # Update the current node
            l1 = l1.next
            l2 = l2.next
            cur_node.next = ListNode(dig_sum)
            cur_node = cur_node.next

        while l1:
            if l1.val + carry < bounder:
                cur_node.next = ListNode(l1.val+carry)
                carry = 0
            else:
                # just set val as 0 in this node
                cur_node.next = ListNode(0)
                carry = 1
            l1 = l1.next
            cur_node = cur_node.next
            if carry>0:
                cur_node.next = ListNode(carry)
        
        while l2:
            if l2.val + carry < bounder:
                cur_node.next = ListNode(l2.val+carry)
                carry = 0
            else:
                # just set val as 0 in this node
                cur_node.next = ListNode(0)
                carry  = 1
            l2 = l2.next
            cur_node = cur_node.next
            if carry>0:
                cur_node.next = ListNode(carry)
        if carry>0:
            cur_node.next = ListNode(carry)
        '''

        '''
        # Method 2
        carry = 0
        bounder = 10
        # blank head node
        head = cur_node = ListNode(0)
        while l1 or l2:
            digit_sum = carry
            if l1:
                digit_sum += l1.val
                l1 = l1.next
            if l2:
                digit_sum += l2.val
                l2 = l2.next
            cur_node.next = ListNode(digit_sum % bounder)
            cur_node = cur_node.next
            carry = int(digit_sum / bounder)
        if carry > 0:
            cur_node.next = ListNode(carry)
        return head.next
        '''

        # Method 3
        carry = 0
        bounder = 10
        # blank head node
        head = cur_node = ListNode(0)
        while l1 or l2 or carry:
            digit_sum = carry
            if l1:
                digit_sum += l1.val
                l1 = l1.next
            if l2:
                digit_sum += l2.val
                l2 = l2.next
            cur_node.next = ListNode(digit_sum % bounder)
            cur_node = cur_node.next
            carry = int(digit_sum / bounder)

        return head.next
            