import re

p=re.compile("[a-z]")

p=re.compile("^pythonl\s\w+")
p=re.compile("python\s\w+")
p=re.compile("")

text='a\nb'
print(text)
p1=re.compile('a.b')
m1=p1.match(text)

p2=re.compile('a,b', re.DOTALL)
m2=p2.match(text)

p3=re.compile('[a-z]+', re.IGNORECASE)
m3=p3.match(text)

p4=re.compile("^python\s\w+", re.MULTILINE)
m4=p4.match(text)

 