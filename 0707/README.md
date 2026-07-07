# 📚 Python Practice Projects

Python을 활용한 데이터 분석, 머신러닝, 자동화 및 기초 프로그래밍 실습
프로젝트입니다.

## 📂 프로젝트 구성

### 1. `practice.ipynb`

**선형 회귀(Linear Regression) 예제**

-   `scikit-learn`의 `LinearRegression` 모델 사용
-   키와 몸무게 데이터를 이용한 선형 회귀 학습
-   새로운 키에 대한 몸무게 예측
-   데이터 시각화

**사용 기술** - Python - NumPy - Matplotlib - Scikit-learn

### 2. `chap15.ipynb`

**Pandas 데이터 분석 실습**

-   Titanic 데이터셋 활용
-   데이터 불러오기
-   데이터 전처리
-   결측치 확인
-   데이터 탐색 및 분석
-   Pandas 기능 실습

**사용 기술** - Python - Pandas - NumPy

### 3. iris.py
붓꽃(Iris) 데이터셋을 이용한 머신러닝 분류 및 3D 데이터 시각화 프로그램

#### 주요 기능
- Scikit-learn의 Iris 데이터셋 로드
- SVM(Support Vector Machine) 모델 학습
- 새로운 샘플 품종 예측
- Plotly를 이용한 3차원 데이터 시각화

#### 사용 기술
- Python
- Pandas
- Scikit-learn
- Plotly
### 4. `news.py`

**축구 경기 기사 자동 생성 프로그램**

사용자가 경기 정보를 입력하면 축구 기사를 자동으로 작성하는
프로그램입니다.

**주요 기능** - 경기 결과 입력 - 기사 자동 생성 - 승패에 따른 기사 내용
변경 - 손흥민 선수의 골/도움 기록 반영 - Windows 음성(TTS)을 이용한 기사
읽기

**사용 기술** - Python - datetime - subprocess - Windows Speech API
(PowerShell)

## 🛠 실행 방법

### 1. 저장소 복제

``` bash
git clone https://github.com/사용자이름/저장소이름.git
cd 저장소이름
```

### 2. 필요한 라이브러리 설치

``` bash
pip install pandas numpy matplotlib scikit-learn
```

### 3. 실행

Jupyter Notebook

``` bash
jupyter notebook
```

또는

``` bash
python iris.py
python news.py
```

## 📦 개발 환경

-   Python 3.x
-   Jupyter Notebook
-   Visual Studio Code

## 📖 학습 내용

-   Pandas 데이터 분석
-   NumPy 기초
-   머신러닝(SVM, Linear Regression)
-   데이터 시각화
-   Python 기초 문법
-   자동화 프로그램 제작
-   Windows 음성 합성(TTS)
