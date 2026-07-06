# Python 기초: `pip`, `install`, `import`, 가상환경(venv)

## 1. `pip`, `install`, `import`란?

파이썬에서 라이브러리를 사용하려면 먼저 설치하고, 코드에서 불러와야 합니다.

| 명령어       | 역할                                   | 사용하는 위치 |
| --------- | ------------------------------------ | ------- |
| `pip`     | 패키지(라이브러리)를 설치 및 관리하는 프로그램           | 터미널     |
| `install` | `pip`에게 패키지를 설치하라고 지시하는 명령           | 터미널     |
| `import`  | 설치된 패키지를 현재 프로그램에서 사용할 수 있도록 불러오는 명령 | 파이썬 코드  |

---

## 2. `pip install`

라이브러리를 컴퓨터에 설치하는 명령입니다.

```bash
pip install numpy
```

의미

* `pip` : 패키지 관리자 실행
* `install` : 설치 명령
* `numpy` : 설치할 라이브러리 이름

다른 예시

```bash
pip install pandas
pip install requests
pip install matplotlib
```

> 라이브러리는 한 번만 설치하면 됩니다.

---

## 3. `import`

설치된 라이브러리를 현재 프로그램에서 사용하기 위해 불러옵니다.

```python
import numpy
```

보통은 별칭(alias)을 붙여 사용합니다.

```python
import numpy as np
```

예제

```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr)
```

---

## 4. 전체 사용 과정

### ① 라이브러리 설치

```bash
pip install pandas
```

### ② 코드에서 불러오기

```python
import pandas as pd
```

### ③ 사용하기

```python
import pandas as pd

df = pd.DataFrame({
    "이름": ["철수", "영희"],
    "나이": [20, 21]
})

print(df)
```

---

## 5. `pip install`과 `import`의 차이

### `pip install`

* 컴퓨터에 라이브러리를 설치
* 터미널에서 실행
* 한 번만 실행하면 됨

예시

```bash
pip install requests
```

### `import`

* 설치된 라이브러리를 현재 프로그램으로 불러옴
* 파이썬 코드에서 실행
* 프로그램 실행할 때마다 필요

예시

```python
import requests
```

---

## 비유

**pip install**

> 서점에서 책을 사서 책장에 꽂는 것

**import**

> 책장에서 책을 꺼내 읽는 것

---

# Python 가상환경(Virtual Environment)

## 1. 가상환경이란?

가상환경(Virtual Environment)은 프로젝트마다 독립적인 파이썬 환경을 만드는 기능입니다.

예를 들어

* 프로젝트 A → NumPy 1.x 사용
* 프로젝트 B → NumPy 2.x 사용

처럼 서로 다른 버전의 라이브러리를 사용할 수 있습니다.

### 장점

* 프로젝트별 라이브러리 관리
* 버전 충돌 방지
* 협업이 쉬워짐
* 배포가 편리함

---

## 2. 가상환경 생성

프로젝트 폴더에서 실행합니다.

```bash
python -m venv venv
```

또는

```bash
python3 -m venv venv
```

설명

* `python`
* `-m`
* `venv`
* `venv` : 생성될 폴더 이름

예시

```bash
python -m venv myenv
```

그러면

```
myenv/
```

폴더가 생성됩니다.

---

## 3. 가상환경 활성화

### Windows CMD

```bash
venv\Scripts\activate
```

### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
source venv/bin/activate
```

활성화되면

```text
(venv) C:\Users\User\project>
```

또는

```text
(venv) user@computer:~/project$
```

처럼 `(venv)`가 표시됩니다.

---

## 4. 패키지 설치

가상환경이 활성화된 상태에서 설치합니다.

```bash
pip install numpy
pip install pandas
pip install requests
```

설치된 패키지 확인

```bash
pip list
```

---

## 5. 프로그램 실행

```bash
python
```

또는

```bash
python main.py
```

---

## 6. 가상환경 종료

```bash
deactivate
```

---

# 전체 작업 순서

```bash
# 프로젝트 생성
mkdir myproject
cd myproject

# 가상환경 생성
python -m venv venv

# 가상환경 활성화

# Windows(CMD)
venv\Scripts\activate

# Windows(PowerShell)
venv\Scripts\Activate.ps1

# macOS/Linux
source venv/bin/activate

# 라이브러리 설치
pip install requests
pip install pandas

# 프로그램 실행
python main.py

# 작업 종료
deactivate
```

---

# 패키지 목록 저장

현재 설치된 라이브러리 목록을 저장합니다.

```bash
pip freeze > requirements.txt
```

생성되는 파일

```
requirements.txt
```

예시

```text
numpy==2.3.0
pandas==2.3.1
requests==2.32.3
```

---

# 다른 컴퓨터에서 동일한 환경 만들기

먼저 가상환경을 생성하고 활성화한 뒤,

```bash
pip install -r requirements.txt
```

를 실행하면 `requirements.txt`에 기록된 라이브러리가 모두 설치됩니다.

---

# 핵심 정리

| 명령어                               | 설명                             |
| --------------------------------- | ------------------------------ |
| `pip install 패키지명`                | 라이브러리 설치                       |
| `import 패키지명`                     | 라이브러리 사용                       |
| `python -m venv venv`             | 가상환경 생성                        |
| `venv\Scripts\activate`           | Windows(CMD)에서 가상환경 활성화        |
| `venv\Scripts\Activate.ps1`       | Windows(PowerShell)에서 가상환경 활성화 |
| `source venv/bin/activate`        | macOS/Linux에서 가상환경 활성화         |
| `pip list`                        | 설치된 패키지 확인                     |
| `pip freeze > requirements.txt`   | 패키지 목록 저장                      |
| `pip install -r requirements.txt` | 패키지 목록으로 설치                    |
| `deactivate`                      | 가상환경 종료                        |
