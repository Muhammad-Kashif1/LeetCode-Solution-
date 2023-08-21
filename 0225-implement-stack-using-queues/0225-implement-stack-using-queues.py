from collections import deque

class MyStack:

    def __init__(self):
        self.Q1 = deque()

    def push(self, x):
        # For pushing any element, just push it into Q1
        self.Q1.append(x)

    def pop(self):
        # Implement reversing the queue
        size = len(self.Q1)
        x = None
        while size > 1:
            x = self.Q1.popleft()
            self.Q1.append(x)
            size -= 1
        x = self.Q1.popleft()
        return x

    def top(self):
        return self.Q1[-1]

    def empty(self):
        return not bool(self.Q1)
