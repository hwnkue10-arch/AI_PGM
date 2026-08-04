# C++ 함수(Function) 실습

## 프로젝트 소개

이 프로젝트는 **C++ 함수(Function)**의 기본 개념을 학습하기 위한 예제입니다.

총 2개의 프로그램으로 구성되어 있으며, 함수 선언, 함수 호출, 배열 전달, 반환값 등을 연습할 수 있습니다.

---

# 실습 1 : 함수 호출

## 설명

사용자로부터 두 개의 정수를 입력받아

* 더 큰 값을 찾고
* 그 값이 3의 배수인지 확인하는 프로그램입니다.

## 사용 함수

### `bigger(int a, int b)`

두 개의 정수를 비교하여 큰 값을 반환합니다.

```cpp
int bigger(int a, int b);
```

### `dividedBy3(int n)`

정수가 3의 배수인지 검사합니다.

```cpp
bool dividedBy3(int n);
```

반환값

* `true` : 3의 배수
* `false` : 3의 배수가 아님

### 실행 예시

```text
두 개의 정수 입력 >> 10 15

10와 15중 큰 값은 15입니다.
15은 3의 배수입니다.
```

---

# 실습 2 : 배열과 함수

## 설명

배열을 함수의 매개변수로 전달하여

* 배열의 합 계산
* 배열 값 2배 증가
* 배열 출력

을 수행하는 프로그램입니다.

## 사용 함수

### `addArray(int a[], int size)`

배열의 모든 원소를 더하여 합을 반환합니다.

```cpp
int addArray(int a[], int size);
```

---

### `makeDouble(int a[], int size)`

배열의 모든 원소를 2배로 변경합니다.

```cpp
void makeDouble(int a[], int size);
```

---

### `printArray(int a[], int size)`

배열의 모든 원소를 출력합니다.

```cpp
void printArray(int a[], int size);
```

### 실행 예시

```text
배열 n의 합은 15입니다.
2 4 6 8 10
```

---

# 학습 내용

이 실습을 통해 다음 내용을 학습할 수 있습니다.

* 함수(Function)의 선언과 정의
* 함수 호출
* 반환값(Return Value)
* `bool` 자료형 사용
* 배열을 함수의 매개변수로 전달하기
* 배열 원소 수정
* 반복문(`for`) 활용

---

# 사용 기술

* C++
* 함수(Function)
* 배열(Array)
* 반복문(`for`)
* 조건문(`if`)
* 입출력(`cin`, `cout`)

---

# 실행 환경

* IDE : Visual Studio
* Language : C++
* Console Application

---

# 제작 목적

C++ 함수의 기본 사용법과 배열을 함수의 매개변수로 전달하는 방법을 학습하기 위한 실습 프로그램입니다.
