class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty, no items to pop")
        else:
            self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty, no items to peek")

        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
