from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, item) -> object:
        return self.buffer.appendleft(item)

    def dequeue(self):
        if self.is_empty():
            print("Full")
            return None
        return self.buffer.pop()

    def front(self):
        if self.is_empty():
            print("nothing")
            return None
        return self.buffer[-1]  # Since using appendLeft, so front valur of self.buffer is -1

    def is_empty(self):
        return len(self.buffer) == 0


bi_seq = Queue()


def binary_seq(number):
    binary_num_1 = "1"
    bi_seq.enqueue(binary_num_1)
    for i in range(number):
        front = bi_seq.front()
        bi_seq.enqueue(front + "0")
        bi_seq.enqueue(front + "1")
        new_seq = bi_seq.dequeue()
        print(new_seq)


binary_seq(10)
