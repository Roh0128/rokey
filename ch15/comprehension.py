# [표현식 for 변수 in 이터러블 if 조건]
numbers=[1,2,3,4]
squard=[x**2 for x in numbers ]
print(squard)
print(type(squard))
# 조건문이 참일 경우 요소를 포함하여 표현식 수행
numbers= [1,2,3,4]
even_numbers=[x**2 for x in numbers if x%2==0]
even_numbers=[x**2+1 for x in numbers if x%2==0]
print(even_numbers)

# 딕셔너리 컴프리헨션
# {key:value, key:value, key:value}
# 숫자를 키로, 숫자의 제곱을 값으로 하는 딕셔너리 생성
squared_dict={
    x:x**2 
    for x in range(5)
    }
print(squared_dict)
# 짝수만 포함하는 딕셔너리 생성
even_squared_dict={
    x:x**2 
    for x in range(10) 
    if x %2==0
    }
print(even_squared_dict)


# 제너레이터 컴프리헨션
# (표현식 for 요소 in 이터러블 if 조건)
gen= (i*i for i in range(1,100))
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))
for item in gen:
    print(item)
print(next(gen))

t=tuple(i*i for i in range(1,100))
print(t)
print(type(t))

bad_words=["spam","ad", "click", "promo"]
import re
pattern="|".join([re.escape(word) for word in bad_words])
print(pattern)
text='this is a spam message with promo content'
match_obj=re.findall(pattern, text)
print(match_obj)