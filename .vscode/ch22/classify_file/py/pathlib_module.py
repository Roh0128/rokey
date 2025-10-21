from pathlib import Path

# print(Path.cwd())  #클래스메서드
# print("----------------------------------")
# path=Path(r"ch22\classify_file")
# print(path/ 'file.txt')  #경로 생성 및 조작
# print("----------------------------------")
# file=r"ch22\classify_file"
# path=Path(file)
# print(path.exists())  #존재 여부 확인
# print(path.is_file())  #존재 및 파일 여부 확인
# print(path.is_dir()) #디렉토리 여부 확인
# print("----------------------------------")

# # 디렉토리 생성 및 삭제
# new_folder=r"ch22\classify_file\new_folder"
# path=Path(new_folder)
# path.mkdir(exist_ok=True)  #폴더 생성
# path.rmdir()
# print("----------------------------------")
# # 파일 생성 및 삭제
# file=r"ch22\classify_file\file.txt" 
# file_path=Path(file)
# file_path.touch()   #빈 파일 생성
# file_path.unlink()  #파일 삭제

# # 파일 및 폴더 목록 조회
# dir=r"ch22\classify_file"
# path=Path(dir)
# for item in path.iterdir():
#     print(item)

# file=r"ch22\classify_file\file.txt"
# path=Path(file)
# print(path.suffix)


file=r"ch22\classify_file\file.txt"
path=Path(f"{file}/old_name.txt")
path.touch()   #파일 생성
path.rename(f"{file}/new_name.txt")


