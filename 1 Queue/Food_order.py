import threading
import time
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    # inserting into a queue
    def enqueue(self, item):
        self.buffer.appendleft(item)

    # Pop the order out the queue
    def dequeue(self):
        if len(self.buffer) == 0:
            print("1 Queue is empty")
            return
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0


orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
order_queue = Queue()


def place_order(order):
    for i in order:
        print("Place an order is: ", i)
        order_queue.enqueue(i)
        time.sleep(0.5)


def server_order():
    time.sleep(1)
    while not order_queue.is_empty():
        serve_order = order_queue.dequeue()
        print("Now serving: ", serve_order)
        time.sleep(2)


# Initial multi-threading
t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=server_order)  # No arguments because of "def server_order()"

# Start
t1.start()
t2.start()
# End
t1.join()
t2.join()
