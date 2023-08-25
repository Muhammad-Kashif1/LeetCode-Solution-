# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(left, right):
            # Base case: If left index is greater than right index, return None
            if left > right:
                return None
            
            # Find the middle element of the current subarray
            mid = left + (right - left) // 2
            
            # Create a TreeNode with the middle element as the root
            root = TreeNode(nums[mid])
            
            # Recursively build the left and right subtrees
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
        
        # Call the helper function with initial indices
        return helper(0, len(nums) - 1)
