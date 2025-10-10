# 알아서 문을 닫아주는 똑똑한 방
path=r"C:\Users\jhroh\OneDrive\rokey\ch12\file1.txt"
with open(path, "w",encoding="utf-8") as f:

    f.write("with 구문을 사용하면 자동으로 닫힙니다")
    print("파일에 내용을 쓰는 중")

print("파일 작업 완료(자동으로 닫힘)")

# close가 필요 없음
# %연산자 사용 방식: 문자열 하나로 묶고 %연산자 뒤에 ()와 변수값을 넣어주는 형태
# %s:문자열, %d:십진수, %f:실수형, %x:십육진수 %o: 팔진수
name,age="홍길동",551
print("이름:%s,나이:%d"%(name, age))

# f-string
print(f"{name}, {age}")

# format
print("이름:{name} 나이:{age}".format(name,age))

lines=["첫째 줄\n","둘째 줄\n","셋째줄 \n"]
for i, line in enumerate(lines):
    print(f"{i}번째 {line.strip()}")
    # 23