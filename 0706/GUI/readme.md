# 🎨 Paint

Tkinter를 이용해 만든 간단한 그림판 프로그램입니다.

## 기능

- 펜
- 지우개
- 색상 선택
- 전체 지우기

## 실행 방법

### 1. 저장소 클론

```bash
git clone https://github.com/사용자이름/Paint.git
cd Paint
```

### 2. Python 설치

Python 3.10 이상을 설치합니다.

### 3. 프로그램 실행

```bash
python paint.py
```

## 실행 파일(EXE) 만들기

PyInstaller를 설치합니다.

```bash
pip install pyinstaller
```

실행 파일 생성

```bash
pyinstaller -F -w paint.py
```

생성된 실행 파일은

```
dist/paint.exe
```

에서 확인할 수 있습니다.

## 사용 라이브러리

- tkinter (Python 기본 포함)
