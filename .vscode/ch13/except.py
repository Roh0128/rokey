path=r'C:\Users\jhroh\OneDrive\rokey\hw\계좌1.txt'
mode='r'
with open(path,mode,encoding="utf-8")as f:
    lines=f.readlines()

    accountlist=[] #accountdict={}
    for line in lines:
        linelist=line.split()
        print(linelist[1])
        accountlist.append(linelist[1])

print(accountlist)

# for key, val in accountdict.items():
#    print(f"{key}:{val}")