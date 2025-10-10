# 문자열을 인수로 받아 괄호의 짝이 올바르게 사용되었는지 확인하는 프로그램
def check(text):
    stack=[]
    pairs={')':'(','[':']','{':'}'}
    
    for chat in text:
        if chat in '([{':
            stack.append(char)
        elif chat in ')]}':
            if not stack:
                return False
            if stack.pop() != pairs[chat]:
                return False


    return not stack

# 1. 빈 스택을 생성
# 2. 표현식 내 문자를 가져와(반복)
# 3.만약, 문자에 "시작하는 괄호가 있다면" 스택에 푸시
# 4.끝나는 괄호가 있다면 스택에서 팝
# 4-1: 만약, 스택이 비었다면  False
# 4-2: pop한 괄호를 확인하여 모두 서로 일치하지 않으면 False
# 5.스택이 비어있다면 True

def check_brackets(expression):
    stack=[]
    for char in expression:
        if char in '({[':
            stack.append(char)
            print(f"stack={stack}")
        elif char in ')}]':
            if not stack:
                return False
            top=stack.pop()
            print(f"stack={stack}")

            if  (char==')' and top != ')') or \
                (char==')' and top != ')') or \
                (char==')' and top != ')'):
                return False
        return len (stack)==0

print(check_brackets("(a+b)"))
print(check_brackets("(a+b]}"))
print(check_brackets("[{(x+y)+3}-4]"))
