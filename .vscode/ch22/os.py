import os
print("현재 작업 디렉토리:", os.getcwd())
# 작업 디렉토리 변경
os.chdir(r"C:\Users\jhroh\OneDrive\rokey\ch22")
print('변경된 작업 디렉토리', os.getcwd())

print('현재 디렉토리 목록', os.listdir("."))

# print('디렉토리 생성', os.mkdir('test_dir'))

print("디렉토리 삭제", os.rmdir("test_dir"))

# 파일 존재 여부 확인
if os.path.exists("file.txt"):
    print("파일이 존재합니다")

