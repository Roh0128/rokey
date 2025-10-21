try:
    path=r'C:\Users\jhroh\OneDrive\rokey\ch13\exception\myfile.txt'
    # f= open(path,'w')
    f=open(path)
    s=f.readline()
    i=int(s.strip())
except (RuntimeError, TypeError, NameError):
    print("runtimeError, TypeError,NameError중 하나의 예외 발생시 처리 구문")
except FileNotFoundError:
    print( "파일을 찾을 수 없습니다")
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("정수형으로 변환 불가")
except Exception as e:
    print(f"unexcpected {e}, {type(e)}")