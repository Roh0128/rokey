class MyRange:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        elif self.step < 0 and self.current <= self.stop:
            raise StopIteration
        
        result = self.current
        self.current += self.step
        return result

# 테스트
print("MyRange(1, 10, 2):")
for i in MyRange(1, 10, 2):
    print(i, end=' ') # 1 3 5 7 9

print("\nMyRange(5, 0, -1):")
for i in MyRange(5, 0, -1):
    print(i, end=' ') # 5 4 3 2 1