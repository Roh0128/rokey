#  회전 큐 구현
from collections import deque

def rotate_queue(items, k):
    dq=deque(items)
    # dq.rotate(-k)
    for _ in range(k):
        dq.append(dq.popleft())
    # dq.appendleft(cirque)

    return list(dq)







data=[1,2,3,4,5]
k=2
print(rotate_queue(data,k))
# [3,4,5,1,2]