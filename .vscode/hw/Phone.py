class Phone:
    def __init__(self,number,color):
        self.number=number
        self.color=color
    def showinfo(self):
        print(self.number,self.color)

class SmartPhone(Phone):
    def __init__(self,number,color,company):
        super().__init__()
        self.company=company
    def showinfo(self):
        super.showinfo()
        print("회사",self.company)

 

