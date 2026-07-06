#10.Remove one element from the front of the queue and display the updated queue.
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
print("original queue:", queue)
delt = queue.popleft()
print("delt element:", delt)
print("updated queue:", queue)