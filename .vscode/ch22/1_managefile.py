import os
import shutil

def list_text_files(folder_path):





    f_list=[]
    files=os.listdir(folder_path)
    
    for file in files:
        if file[-4]==".txt":
            f_list.append(file)

    return f_list




if __name__ == "__main__":
    folder=r"C:\Users\jhroh\OneDrive\rokey\ch22\manage_file\folder1"
    if not os.path.exists(folder):
        os.mkdir(folder)

    file1=f"{folder}/file1.txt"
    file2=f"{folder}/file2.txt"

    with open(file1,'w') as f:
        f.write("file1\n")
    with open(file2,'w') as f:
        f.write("file2\n")





    source=r"C:\Users\jhroh\OneDrive\rokey\ch22\manage_file\folder1"
    print("파일 목록", list_text_files(source))