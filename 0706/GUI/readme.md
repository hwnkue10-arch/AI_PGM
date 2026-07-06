## 실행 파일(EXE) 생성 방법

### 1. PyInstaller 설치

터미널(CMD, PowerShell 또는 VS Code 터미널)을 열고 다음 명령어를 실행합니다.

```bash
pip install pyinstaller
```

또는

```bash
python -m pip install pyinstaller
```

---

### 2. 프로젝트 폴더로 이동

```bash
cd 프로젝트_폴더
```

예시

```bash
cd D:\PythonProject
```

---

### 3. 실행 파일 생성

GUI 프로그램(Tkinter)의 경우 아래 명령어를 실행합니다.

```bash
python -m PyInstaller -F -w 파일이름.py
```

예시

```bash
python -m PyInstaller -F -w calculator.py
```

```bash
python -m PyInstaller -F -w paint.py
```

```bash
python -m PyInstaller -F -w notepad.py
```

옵션 설명

- `-F` : 하나의 실행 파일(.exe)로 생성
- `-w` : 콘솔(CMD) 창을 표시하지 않음 (Tkinter GUI 프로그램에 권장)

---

### 4. 실행 파일 확인

빌드가 완료되면 프로젝트 폴더에 다음과 같은 파일과 폴더가 생성됩니다.

```
build/
dist/
파일이름.spec
```

생성된 실행 파일은 `dist` 폴더 안에서 확인할 수 있습니다.

예시

```
dist/
 ├── calculator.exe
 ├── paint.exe
 └── notepad.exe
```

---

### 참고

`build` 폴더와 `.spec` 파일은 빌드 과정에서 생성되는 파일이므로 삭제해도 됩니다.

GitHub에는 일반적으로 소스 코드(`.py`)만 업로드하며, `build`, `dist`, `.spec` 파일은 업로드하지 않는 것을 권장합니다.
