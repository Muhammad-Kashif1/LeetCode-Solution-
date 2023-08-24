class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        current = root

        while current:
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                # Find the predecessor node (rightmost node in the left subtree)
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                if not predecessor.right:
                    predecessor.right = current  # Thread the predecessor to the current node
                    current = current.left
                else:
                    predecessor.right = None  # Remove the thread
                    result.append(current.val)
                    current = current.right

        return result
