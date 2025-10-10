import os

# 파일을 쓰기 모드('w')로 엽니다.
f = open(r"C:\Users\jhroh\OneDrive\rokey\ch12\file1.txt", "w",encoding='utf-8')

# 파일에 내용을 씁니다.(모두 지우고)
f.write("파이썬 파일 처리 공부 중입니다.\n")
f.write("두 번째 줄입니다.\n")

for i in range(1,11):
    data="%d번째 줄입니다.\n"%i#f"{i}번째 줄입니다"
    f.write(data)

# ★★★ 파일을 닫아서 변경 내용을 최종 저장합니다. ★★★
f.close()

print("파일 쓰기 및 저장이 완료되었습니다.")

# 인코딩=텍스트에서 바이너리
# 디코딩=바이너리에서 텍스트

# 고급언어=사람이 이해하기 쉬운
# 저급언어=컴퓨터의 이해에 가까운

# "A"=65
# "a"=97
# "가"=AC00
text='A'
text='a'
text='가'
print(ord(text))

print(chr(65))
