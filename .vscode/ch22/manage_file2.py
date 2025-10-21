from pathlib import Path

def get_files(folder_path):
    # "특정 폴더 내의 모든 파일 목록을 반환"
    # "param folder_path":검색할 폴더 경로
    # :return:파일 리스트

    f_list=[]
    folder=Path(folder_path)

    for file in folder.iterdir():
        # print(file)
        f_list.append(file)

    return f_list


def organize_file_by_extension(source_folder):
    """특정 폴더 내의 파일을 확장자별로 폴더를 생성하여 이동
    param source_folder: 정리할 폴더 경로"""
    source=Path(source_folder)
    if not source.exists():
        print("폴더가 존재하지 않음")
        return
    # 특정 폴더의 파일 가져오기
    for file in get_files(source):
        # 확장자 체크
        # print(file.suffix[1:])
        extension=file.suffix[1:]
        print(extension)
        
        ext_folder=source / extension
        # 확장자 이름으로 디렉터리 생성
        ext_folder.mkdir(exist_ok=True)
        # 확장자 이름 디렉터리에 파일 이동
        file.rename(ext_folder / file.name)
        print(f"파일 이동 완료:{file.name}->{ext_folder}")

if __name__=="__main__":
    source=r"ch22\classify_file"
    print("1.파일 목록:")
    print(get_files(source))
    print("2.파일을 확장자별로 정리 중...")
    organize_file_by_extension(source)