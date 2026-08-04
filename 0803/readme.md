# C++ 기초 및 객체지향 프로그래밍 학습 리포지토리

이 리포지토리는 C++ 프로그래밍 언어의 기본 문법부터 객체지향 프로그래밍(OOP) 핵심 개념까지 학습한 실습 코드들을 모아둔 공간입니다.

---

## 📌 주요 학습 내용

### 1. C++ 기본 문법 및 입출력 (Basics & I/O)
* **표준 입출력**: `cin`, `cout`을 이용한 데이터 입력 및 출력 처리
* **변수 범위 (Scope)**: 전역 변수(Global Variable)와 지역 변수(Local Variable)의 차이 및 전역 함수 작성법
* **연산자 활용**: 산술, 시프트(`<<`), 비교, 모듈러, 삼항 연산자, `sizeof`, 증감, 복합대입, 비트 논리(`&`), 쉼표(Comma) 연산자 실습
* **제어문 & 반복문**: `for`, `while`, `do-while` 반복문 실습 및 C++ 연산 구조 이해 (Python 반복문과의 연산 구조 비교 모의 수록)

### 2. 문자열 및 배열 다루기 (Strings & Arrays)
* **C-style 문자열 입력/처리**: `cin.getline()`을 활용한 공백 포함 문자열 입력 처리
* **문자 탐색 및 카운팅**: `while` 문과 널 문자(`\0`) 조건 검사를 통한 문자열 길이 측정 및 특정 문자의 개수 세기
* **배열 및 데이터 관리**: 배열 구조를 활용한 사용자 지정 구조적 데이터(학번 및 이름 등) 입력/출력 관리

### 3. 객체지향 프로그래밍 (OOP Concepts)
* **클래스와 객체 (Class & Object)**: `Circle` 클래스 실습을 통한 멤버 변수와 멤버 함수의 정의 및 구현
* **생성자 오버로딩 (Constructor Overloading)**: `Rectangle` 클래스를 활용한 기본 생성자, 매개변수가 있는 생성자, 단일 매개변수 생성자 구현
* **접근 제어자 (Access Specifiers)**: `private`과 `public` 키워드를 활용한 데이터 캡슐화(Encapsulation) 및 접근 제한 규칙 확인

---

## 📂 파일별 세부 설명

| 파일명 | 주요 개념 | 설명 |
| :--- | :--- | :--- |
| **`01_basics_io.cpp`** | 입출력 및 변수 범위 | 전역/지역 변수 선언과 `cin`, `cout`을 통한 덧셈 프로그램 |
| **`02_class_circle.cpp`** | 클래스 기초 | `Circle` 클래스를 정의하고 반지름에 따른 넓이(`getArea`) 계산 |
| **`03_access_specifiers.cpp`** | 접근 제어자 | `private` 및 `public` 멤버에 대한 클래스 내부/외부 접근 권한 테스트 |
| **`04_string_handling.cpp`** | 문자열 처리 | `cin.getline`을 통한 입력 처리 및 특정 문자의 빈도수 계산 |
| **`05_operators.cpp`** | 다양한 연산자 | 비트 연산, 삼항 연산자, 쉼표 연산자 등 C++ 연산자 종합 실습 |
| **`06_loops_sum.cpp`** | 반복문 | `for`, `while`, `do-while` 문을 이용한 구간 합계 구하기 |
| **`07_arrays_student.cpp`** | 배열 활용 | 학번과 이름을 배열로 받아 출력하는 학생 정보 관리 예제 |
| **`08_constructor_overloading.cpp`** | 생성자 오버로딩 | `Rectangle` 클래스의 다양한 생성자 오버로딩 및 정사각형 판별 |

---

## 🛠️ 개발 및 실행 환경

* **언어 (Language)**: C++ (C++11 이상 권장)
* **IDE / 컴파일러 (Environment)**: Visual Studio / GCC / Clang
* **빌드 및 실행 (Terminal)**:
  ```bash
  # g++ 컴파일 예시
  g++ -o main 01_basics_io.cpp
  ./main
  ```

---

## 💡 주요 개념 요약 노트

### 🔒 Access Specifiers (접근 제어자)
* `private`: 클래스 내부 멤버 함수에서만 접근이 가능하며, 외부 객체 direct access 시 컴파일 에러 발생
* `public`: 클래스 외부 어디서나 접근 가능

### 🔄 Constructor Overloading (생성자 오버로딩)
```cpp
Rectangle();            // 기본 생성자 (width=1, height=1)
Rectangle(int w, int h); // 매개변수 2개 생성자
Rectangle(int length);  // 매개변수 1개 생성자 (정사각형)
```
