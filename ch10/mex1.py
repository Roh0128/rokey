class Cvalue:
    def __init__(self):
        self.lista=[]
    def add(self,num):
        self.lista.append(num)
    def fprint(self):
        print(self.lista)
def plus(a,b):
    c=a+b
    return c
str1='hello'
print(__name__)

if __name__=="__main__":
    p1=Cvalue()
    p1.add(11)
    p1.add(21)
    p1.add(31)
    p1.fprint()




