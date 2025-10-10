import time
def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

list_job=(longtime_job() for i in range(5)) #or []
# print(list_job[0])

print(next(list_job))

for i in range(5):
    longtime_job()


food=["김밥","만두","양념치킨","족발","쫄면","라면"]
ifoods=iter(food)
print(type(ifood))

for i in range(len(food)):
    print(next(ifood))
print(next(ifood))

for i in ifood:
    print(i)
print(next(ifood))

file_path=
data=
def write_file(file_path):
    with open(file_path, 'w') as file:
        file.write(data)
# readline() 파일에서 한줄씩 읽기
with open(file_path, 'r') as file:
    file.readline()

# 컴프리핸션,yield
def read_file(file_path):
    with open(file_path,'r') as file:
        for line in file.readlines():
            yield line

lines= read_file(file_path)
print(type(lines))
for line in lines:
    print(line)