class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        queue_p = [p]
        queue_q = [q]
        
        while queue_p and queue_q:
            node_p = queue_p.pop(0)
            node_q = queue_q.pop(0)
            
            if not node_p and not node_q:
                continue  # Both nodes are None, move to the next pair
            
            if not node_p or not node_q:
                return False  # One node is None while the other is not
            
            if node_p.val != node_q.val:
                return False
            
            queue_p.append(node_p.left)
            queue_p.append(node_p.right)
            
            queue_q.append(node_q.left)
            queue_q.append(node_q.right)
        
        return True
