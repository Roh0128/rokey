import shutil
import os

path=r"C:\Users\jhroh\OneDrive\rokey\ch22\test_dir"
src=f"{path}/file.txt"
dst=f"{path}/copiedfile.txt"
# file 복사
if not os.path.exists(dst):
    shutil.copy(src,dst)
    shutil.copy2(src,dst)

folder= f"{path}/test_dir"
if not os.path.exists(folder):
    os.mkdir(folder)

src=f"{path}/file.txt"
dst=f"{path}/test_dir/file.txt"
if not os.path.exists(dst):
    shutil.copy(src,dst)



# 디렉토리 복사
src=f"{path}/test_dir"
dst=f"{path},copiedfile.txt"
if not os.path.exists(dst):
    shutil.copytree(src,dst)    

# 파일 및 디렉토리 이동
src=f"{path}/copiedfile.txt"
dst=f"{path}/copied_test_dir/copiedfile.txt"
if not os.path.exists(dst):
    shutil.move(src,dst)

#  파일 및 디렉토리 삭제
dir1=f"{path}/text_dir"
dir2=f"{path}/copied_test_dir"
shutil.rmtree(dir1)
shutil.rmtree(dir2)

