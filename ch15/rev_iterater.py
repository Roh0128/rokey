class ReverseIterator:
    def __init__(self,data):
        self.data=data
        self.position=len(self.data)-1

    def __iter__(self):
        return self
    def __next__(self):
        if self.position <0:        
            raise StopIteration
        result= self.data
        self.position -=1
        return result