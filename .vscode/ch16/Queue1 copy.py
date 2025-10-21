# 선입선출 형태로 데이터 처리
class Queue:
    def __init__(self):
        self.queue=[]
# enqueue 기능
    def enqueue(self,data):
        self.queue.append(data)
# dequeue 기능
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return
    # 큐 상태 확인
    def is_empty(self):
        if len(self.queue) ==0:
            return True
        return False
    # 큐 상태 확인
    def status_queue(self):
        return self.queue
q1=Queue()
q1.dequeue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.dequeue()
print(q1.status_queue())
