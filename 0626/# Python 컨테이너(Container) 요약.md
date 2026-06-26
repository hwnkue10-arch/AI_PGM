# Python 컨테이너(Container) 요약

파이썬의 컨테이너는 여러 개의 데이터를 저장하고 관리하는 자료구조입니다.  
대표적으로 **list, tuple, set, dict** 등이 있으며, 용도와 특징이 다릅니다.

---

## 1. 리스트 (List)

```python
my_list = [1, 2, 3, 4]
특징
순서가 있음 (ordered)
변경 가능 (mutable)
중복 허용
다양한 타입 저장 가능
주요 메서드
append(x): 끝에 추가
remove(x): 값 삭제
pop(): 마지막 요소 제거
sort(): 정렬
2. 튜플 (Tuple)
my_tuple = (1, 2, 3)
특징
순서 있음
변경 불가 (immutable)
중복 허용
빠른 읽기 성능
사용 예
변경되면 안 되는 데이터
함수 반환값 여러 개
3. 집합 (Set)
my_set = {1, 2, 3}
특징
순서 없음 (unordered)
중복 허용 안 함
변경 가능
주요 연산
add(x): 추가
remove(x): 삭제
union(): 합집합
intersection(): 교집합
4. 딕셔너리 (Dict)
my_dict = {"name": "Kim", "age": 20}
특징
key-value 구조
순서 있음 (Python 3.7+)
key는 중복 불가
value는 중복 가능
주요 메서드
keys(): 키 목록
values(): 값 목록
items(): (키, 값) 쌍
get(key): 안전한 접근
5. collections 모듈
deque (양방향 큐)
from collections import deque

q = deque([1, 2, 3])
q.append(4)
q.appendleft(0)
특징
양쪽 끝에서 빠른 삽입/삭제
큐/스택 구현에 적합
6. frozenset
fs = frozenset([1, 2, 3])
특징
set과 같지만 immutable
dictionary key로 사용 가능
7. 요약 비교
자료구조	순서	변경 가능	중복 허용	특징
list	O	O	O	일반적 배열
tuple	O	X	O	고정 데이터
set	X	O	X	중복 제거
dict	O	O	key X	key-value
frozenset	X	X	X	immutable set
8. 언제 무엇을 사용할까?
리스트 → 순서 있는 데이터 모음
튜플 → 변경되면 안 되는 데이터
세트 → 중복 제거, 집합 연산
딕셔너리 → 키로 빠르게 조회
deque → 큐/스택 구조 필요할 때