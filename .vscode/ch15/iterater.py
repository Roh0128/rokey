class Myiterater:
    # 클래스 내부의 메서드는 4칸 들여쓰기
    def __init__(self, data):
        # 메서드 내부의 코드는 8칸 들여쓰기
        self.data = data
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result


if __name__ == "__main__":
    # if 블록 내부의 코드는 4칸 들여쓰기
    i = Myiterater([1, 2, 3])
    print(next(i))
    print(f"위치:{i.position}")
    for item in i:
        # for 루프 내부의 코드는 8칸 들여쓰기
        print(item)
        print(f"위치:{i.position}")
    
    # 이 부분은 for 루프가 끝난 후 실행되므로 4칸 들여쓰기
    print(next(i))