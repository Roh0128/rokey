class Stack:
    def __init__(self, initial_list=None):
        self.items = initial_list if initial_list else []

    def push(self, item):
        self.items.append(item)

my_list = ['두산', '로키', '부트']
stack = Stack(my_list)
stack.push('캠프')
print(stack.items) # 결과: ['두산', '로키', '부트', '캠프']


class Stack:
    # (이전 코드와 동일)
    def __init__(self, initial_list=None):
        self.items = initial_list if initial_list else []
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

my_list_with_camp = ['두산', '로키', '부트', '캠프']
stack = Stack(my_list_with_camp)
stack.pop()
print(stack.items) # 결과: ['두산', '로키', '부트']