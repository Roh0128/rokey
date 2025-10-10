import re

# 패턴객체=re.compile(정규표현식)
# 매치객체.match("검색대상문자열")
# print(매치객체)

p=re.compile("[abc]")
p=re.compile("[abc][abc]")
m=p.match("banana")
print(m)

p=re.compile("a")
p=re.compile("b")
p=re.compile("ba")
p=re.compile("ab")
m=p.match("banana")
print(m)


p=re.compile("[\^]")
# 메타문자
# []
# .
# *
# {}
# ?
# ^
# $

p=re.compile("[a-z]")
m=p.match("Apple")
print(m)

p=re.compile("[A-Z]")
m=p.match("Apple")
m=p.match("banana")
# whitespace
# \r= 현재 줄 맨 앞으로 이동
# \f= 다음페이지로 넘김
# \v=수직 탭
# \s= 화이트스페이스 문자와 매치
p=re.compile("\s")
print(p.match("Apple"))
print(p.match("banana"))
print(p.match("_melon"))
print(p.match(" orange"))
print(p.match("\torange"))
print(p.match("\norange"))
print(p.match("\rorange"))
#  \d= [0-9]
# \D=[^0-9]
# \w= 문자+숫자와 매치
# \W=문자+숫자가 아닌 문자와 매치
p=re.compile("\d")
print(p.match("Apple"))
print(p.match("2banana"))

p=re.compile("[^0-9abc]")
p=re.compile("[abc\D]")

print(p.match("3banana"))

p=re.compile("a,b")
print(p.match("apple"))
print(p.match("apbple"))

p=re.compile("a..p")
print(p.match("apbple"))

p=re.compile("a,b")
print(p.match("aab"))
print(p.match("abb"))
print(p.match("a0b"))
print(p.match("aOb"))
print(p.match("abb"))
print(p.match("abc"))

print(p.match("a\nb"))
print(p.match("a\rb"))


p=re.compile("ca{2}t")
print(p.match("ct"))
print(p.match("caat"))
print(p.match("caaat"))

p=re.compile("ca{,4}t")
p=re.compile("ca{2,}")

p=re.compile("^Hello")
p=re.compile("Hello$")

m=p.search("python")
print(m)

text = "Part-A: 100mm, Part-B: 25.5kg"
p= re.compile("[\d]")
m=p.match(text)
print(f"\\d(숫자) 매치 결과: {m}")

p=re.compile("[a-z]+")
print(p.search("8pyt4hon"))
