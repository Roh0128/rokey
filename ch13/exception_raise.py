# try:
#     raise NameError('Hi there')
# except NameError as e:
#     print("NameError 예외 발생!")
#     print(e)
#     print(type(e))

# raise NameError('hi there')


# ord(인수)= 이 문자의 컴퓨터 표현에 해당하는 숫자를 리턴
# chr(인수)= 숫자를 인자로 받아 나타내는 문자를 리턴

# 슬라이싱: muna[2:4], muna[:]

my_list=['apple', 'banana','cherry']
joined_string="_".join(my_list)
# joined_string="/".join(my_list)
joined_string="\t".join(my_list)
print(joined_string)