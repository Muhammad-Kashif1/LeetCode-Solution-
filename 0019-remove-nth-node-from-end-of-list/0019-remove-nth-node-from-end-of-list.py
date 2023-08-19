# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Create a dummy node to handle edge cases where the head needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move the first pointer n+1 steps ahead
        for i in range(n + 1):
            first = first.next
        
        # Move both pointers until the first pointer reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Now, the second pointer is at the node just before the one to be removed
        second.next = second.next.next
        
        return dummy.next
