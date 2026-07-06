#11.Display the front element of the queue without removing it.
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
print("front element:", queue[0])
print("queue:", queue)