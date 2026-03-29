# Python implementations of stacks - List-based implementation and Deque-based implementation 

class ListBasedStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError('pop from empty stack')
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError('peek from empty stack')
    
    def is_empty(self):
        return len(self.stack) == 0


from collections import deque

class DequeBasedStack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError('remove from empty stack')
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError('return peek from empty stack')
    
    def is_empty(self):
        return len(self.stack) == 0
    
stack = ListBasedStack()
stack.push(10)
stack.push(20)
stack.push(30)
assert stack.peek() == 30
assert stack.pop() == 30
assert stack.peek() == 20
assert stack.pop() == 20
assert stack.peek() == 10
assert stack.pop() == 10
assert stack.is_empty() == True

stack = DequeBasedStack()
stack.push(10)
stack.push(20)
stack.push(30)
assert stack.peek() == 30
assert stack.pop() == 30
assert stack.peek() == 20
assert stack.pop() == 20
assert stack.peek() == 10
assert stack.pop() == 10
assert stack.is_empty() == True