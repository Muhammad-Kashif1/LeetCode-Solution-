class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        
        while stack:
            left, right = stack.pop()
            
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            
            # Compare the outer left and outer right nodes and inner left and inner right nodes.
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        
        return True
