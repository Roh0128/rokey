path=r"C:\Users\jhroh\OneDrive\rokey\ch12\file1.txt"
f=open(path,"r",encoding="utf-8")

data=f.readlines()# readline, readlines, read
print(data)

f.close()
