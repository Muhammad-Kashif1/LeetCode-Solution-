class MyQueue:

    def __init__(self):
        self.stack1 = []  # To simulate the back of the queue
        self.stack2 = []  # To simulate the front of the queue

    def push(self, x):
        self.stack1.append(x)

    def _move_elements(self):
        # Move elements from stack1 to stack2 only when stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def pop(self):
        self._move_elements()
        # Pop from stack2
        if self.stack2:
            return self.stack2.pop()
        return None

    def peek(self):
        self._move_elements()
        # Peek at the front element in stack2
        if self.stack2:
            return self.stack2[-1]
        return None

    def empty(self):
        return not (self.stack1 or self.stack2)

# Example usage:
myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())  # Output: 1
print(myQueue.pop())   # Output: 1
print(myQueue.empty()) # Output: False
