def square(x):
    return x **2

numbers=[1,2,3,4,5]
squared_numbers=map(square, numbers)
print(list(squared_numbers))

# map( 함수, 이터러블 객체)
#  꼭 리스트로 변환해서 출력해
data={'a':1, 'b':2, 'c':3}

new_data=dict(map(lambda kv: (kv[0].upper(), kv[1]*10), data.items() ))

print(list(new_data))