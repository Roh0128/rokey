import re
p=re.compile("[a-z]+")
print(p.findall("3py3thon"))

result=p.finditer("life is too short")
result=list(result)

for matchobj in result:
    
    print(matchobj.group())
    print(matchobj.end())
    print(matchobj.start())   

    print(matchobj.span())