from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if self.is_empty():
            print("1 Queue is empty")
        else:
            return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def get_buffer(self):
        return list(self.buffer)


pq = Queue()
pq.enqueue({
    # add dictionary into self
    'company': 'wal mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    # add dictionary into self
    'company': 'wal mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 132
})
pq.enqueue({
    # add dictionary into self
    'company': 'wal mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 135
})

print(pq.get_buffer())
