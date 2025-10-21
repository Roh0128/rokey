# try: 
#     코드블록
# except 예외클래스:
#     코드블록
# except 예외클래스:
#     코드블록

while True:
    try:
        x=int(input("정수를 입력하세요"))
        break
    except ValueError:
        print("정수 입력이 아닙니다. 다시 입력하세요:")

# while True:
#     x=int(input("정수를 입력하세요:"))
#     break

# while True:
#     try:
#         x=int(input("정수를 입력하세요"))
#         break
#     except ValueError as error:
#         print("정수 입력이 아닙니다. 다시 입력하세요")
#         print(error)

