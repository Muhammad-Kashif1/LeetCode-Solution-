# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        # Helper function to find the middle element of the linked list
        def find_middle(left, right):
            slow = left
            fast = left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        # Helper function to convert a sorted linked list into a BST
        def sorted_list_to_bst(left, right):
            if left == right:
                return None
            
            mid = find_middle(left, right)
            root = TreeNode(mid.val)
            root.left = sorted_list_to_bst(left, mid)
            root.right = sorted_list_to_bst(mid.next, right)
            return root
        
        return sorted_list_to_bst(head, None)
