# 🐍 Python List 정리

> 파이썬 리스트(List)를 빠르게 이해하고, 자주 쓰는 기능을 한 번에 정리한 문서입니다.

---

## 목차
- [리스트란?](#리스트란)
- [리스트의 특징](#리스트의-특징)
- [리스트 생성](#리스트-생성)
- [인덱싱과 슬라이싱](#인덱싱과-슬라이싱)
- [값 수정하기](#값-수정하기)
- [자주 쓰는 메서드](#자주-쓰는-메서드)
- [길이 구하기](#길이-구하기)
- [반복문과 함께 사용](#반복문과-함께-사용)
- [정렬](#정렬)
- [리스트 컴프리헨션](#리스트-컴프리헨션)
- [중첩 리스트](#중첩-리스트)
- [예제 모음](#예제-모음)
- [주의할 점](#주의할-점)

---

## 리스트란?

파이썬 리스트는 여러 값을 **순서대로 저장**할 수 있는 자료형입니다.  
값을 추가하거나 수정할 수 있는 **가변 자료형**이며, 서로 다른 타입도 함께 담을 수 있습니다 [web:1][web:10].

```python
numbers =[3][4][5][6][7]
mixed = [1, "hello", 3.14, True]
```

---

## 리스트의 특징

| 특징 | 설명 |
|---|---|
| 순서 있음 | 저장한 순서가 유지됩니다. |
| 변경 가능 | 값을 수정할 수 있습니다. |
| 중복 허용 | 같은 값을 여러 번 넣을 수 있습니다. |
| 다양한 타입 저장 | 숫자, 문자열, 불리언 등을 함께 저장할 수 있습니다. |

```python
data = [10, 20, 20, "python", False]
```

---

## 리스트 생성

리스트는 대괄호 `[]` 또는 `list()` 함수로 만들 수 있습니다 [web:1].

```python
a =[4][5][3]
b = list((4, 5, 6))
c = []
```

---

## 인덱싱과 슬라이싱

리스트는 0부터 시작하는 인덱스를 사용합니다.  
음수 인덱스를 사용하면 뒤에서부터 접근할 수 있습니다 [web:1][web:10].

```python
items = ["a", "b", "c", "d"]

print(items)   # a
print(items[-1])  # d
print(items[1:3]) # ['b', 'c']
print(items[:2])  # ['a', 'b']
print(items[::2]) # ['a', 'c']
```

---

## 값 수정하기

리스트는 특정 위치의 값을 직접 바꿀 수 있습니다 [web:1][web:10].

```python
numbers =[8][9]
numbers = 99[3]
print(numbers)  #[9]
```

---

## 자주 쓰는 메서드

| 메서드 | 설명 | 예시 |
|---|---|---|
| `append()` | 맨 뒤에 한 개 추가 | `nums.append(3)` |
| `insert()` | 원하는 위치에 추가 | `nums.insert(1, 5)` |
| `extend()` | 여러 개 추가 | `nums.extend([4, 5])` |
| `remove()` | 값으로 삭제 | `nums.remove(2)` |
| `pop()` | 인덱스로 삭제 | `nums.pop()` |
| `clear()` | 전체 삭제 | `nums.clear()` |

```python
nums =[4][3]

nums.append(3)      #[5][3][4]
nums.insert(1, 5)   #[7][5][3][4]
nums.extend() #[6][10][5][7][3][4]
nums.remove(5)      #[10][5][6][3][4]
nums.pop()          #[5][6][3][4]
```

---

## 길이 구하기

리스트의 길이는 `len()` 함수로 확인합니다 [web:4][web:6].

```python
items =[8][9]
print(len(items))  # 4
```

---

## 반복문과 함께 사용

리스트는 `for`문과 함께 자주 사용됩니다 [web:1][web:5].

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

인덱스가 필요할 때는 `enumerate()`를 사용할 수 있습니다.

```python
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

---

## 정렬

`sort()`는 원본 리스트를 정렬하고, `sorted()`는 새 리스트를 만듭니다 [web:10].

```python
nums =[6][3][4][5]

nums.sort()
print(nums)  #[3][4][5][6]

new_nums = sorted(nums, reverse=True)
print(new_nums)  #[4][5][6][3]
```

---

## 리스트 컴프리헨션

리스트 컴프리헨션은 짧고 깔끔하게 리스트를 만드는 방법입니다 [web:10].

```python
squares = [x * x for x in range(5)]
print(squares)  #[11][12][6][3]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)  #[13][10][6][4]
```

---

## 중첩 리스트

리스트 안에 또 다른 리스트를 넣을 수 있습니다 [web:10].

```python
matrix = [
   ,[5][3][4]
   ,[7][10][6]
[12][14][13]
]

print(matrix)    #[3][4][5]
print(matrix) # 6[4][3]
```

---

## 예제 모음

### 평균 구하기
```python
scores = 
avg = sum(scores) / len(scores)
print(avg)
```

### 포함 여부 확인
```python
names = ["kim", "lee", "park"]
print("lee" in names)  # True
```

### 중복 제거
```python
items =[5][3][4]
unique_items = list(set(items))
print(unique_items)
```

---

## 주의할 점

- 리스트는 `0`부터 시작합니다.
- `remove()`는 **값 기준**, `pop()`은 **인덱스 기준**입니다.
- `append()`는 한 개 추가, `extend()`는 여러 개를 펼쳐서 추가합니다.
- 반복 중 원본 리스트를 직접 수정하면 예상과 다른 결과가 나올 수 있습니다.

---

## 한 줄 정리

> 파이썬 리스트는 가장 기본적이면서도 실용적인 **가변 순서형 자료구조**입니다.
