class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [(nestedList, 0)]

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            nestedList, i = self.stack[-1]
            self.stack[-1] = (nestedList, i + 1)
            return nestedList[i].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            nestedList, i = self.stack[-1]
            if i == len(nestedList):
                self.stack.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                self.stack[-1] = (nestedList, i + 1)
                self.stack.append((x.getList(), 0))
        return False
