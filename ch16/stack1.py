class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return
    # return스택 내 데이터 유무 확인
    def is_empty(self):
        if len(self.stack)==0:
            return True
        return False
    # 스택 최상위 데이터 확인
    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        return
    def status_stack(self):
        return self.stack


if __name__=="__main__":


    stack=[]

    stack=[1,2,3]
    s1=Stack()
    print(s1.pop())
    stack.append(4)
    print(f"stack={stack}")
    print(s1.peak())
    print(s1.push(1))
    stack.pop()
    print(f"stack1={stack}")
    stack.pop()
    print(f"stack2={stack}")
    stack.pop()
    print(f"stack3={stack}")
    stack.pop()
    print(f"stack4={stack}")
    print(s1.status_stack())

    if stack==[]:
        print("its empty!")


    

