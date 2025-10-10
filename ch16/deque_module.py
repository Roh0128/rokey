# 덱의 활용 사례_ 회전 큐,문자열 회문 검사
from collections import deque

dq=deque()

dq.append(1)
print(dq)

dq.appendleft(2)
print(dq)
print(list(dq))
dq.pop()
print(dq)

dq.popleft()
print(dq)

# 알고리즘 성능 측정
# : 알고리즘의 실행 속도를 평가하는 방식
# 주요 복잡도 예시
# O(1): 상수시간( 배열의 특정 인덱스 접근)
# O(log n): 로그시간 (이진탐색)
# O(n): 선형시간( 리스트 순회)
# O(n log n):로그 선형 시간(퀵 정렬, 병합 정렬)
# O(n^2):이차 시간 (버블 정렬)



# 리스트 구조: 동적 배열 기반
# append와  pop을 사용= O(1), 가끔 크기확장을 위해 O(n)
# deque의 구조: 이중연결 리스트 또는 고정크기 블록 연결 구조
# list.append() vs deque.append() 거의 비슷
# list.pop(0) vs deque.popleft(): 차이 발생
# list.pop(0): O(n)
# deque.popleft(): O(1)