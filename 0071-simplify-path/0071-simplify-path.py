class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path = path.split('/')

        for dir in path:
            if dir == '..':
                if stack:
                    stack.pop()
            elif dir and dir != '.':
                stack.append(dir)

        return '/' + '/'.join(stack)
