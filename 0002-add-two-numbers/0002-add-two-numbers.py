# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        
        # Initialize a dummy head node to simplify the code for the first node
        dummy_head = ListNode()
        current = dummy_head
        
        while l1 or l2 or carry:
            # Get the values of the current nodes or use 0 if one of them is None
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            # Calculate the sum of the values from l1, l2, and the carry
            total = x + y + carry
            carry = total // 10
            
            # Modify l1 to store the result (reuse the original linked list)
            if l1:
                l1.val = total % 10
                current.next = l1
                l1 = l1.next
            else:
                current.next = ListNode(total % 10)
            
            # Move to the next node in l2 if it exists
            if l2:
                l2 = l2.next
            
            current = current.next
        
        return dummy_head.next
