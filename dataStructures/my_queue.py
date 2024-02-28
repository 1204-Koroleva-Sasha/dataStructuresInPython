class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            raise Exception("No items in Queue")

        self.queue.pop(0)

    def peek_front(self):
        if len(self.queue) == 0:
            raise Exception("No items in Queue")

        return self.queue[0]

