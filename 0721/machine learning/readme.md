# TensorFlow & Keras 학습 정리

이 저장소는 TensorFlow와 Keras를 이용한 딥러닝 기초부터 CNN(합성곱 신경망)까지의 학습 예제를 정리한 프로젝트입니다.

## 파일 구성

### 1. 01-first-model.ipynb
**주제:** TensorFlow와 머신러닝 기초

### 학습 내용
- TensorFlow 및 Keras 소개
- 첫 번째 머신러닝 모델 생성
- 데이터 준비 및 학습
- 모델 예측 결과 확인
- 기본적인 딥러닝 학습 과정 이해

---

### 2. 02-fashion-mnist.ipynb
**주제:** Fashion MNIST를 이용한 이미지 분류

### 학습 내용
- Fashion MNIST 데이터셋 사용
- 의류 이미지 분류 모델 구현
- 모델 예측 결과 분석
- Epoch 증가에 따른 성능 변화
- 과대적합(Overfitting) 이해
- Early Stopping을 이용한 학습 종료

---

### 3. 03-beyond-the-basics.ipynb
**주제:** CNN(합성곱 신경망)과 이미지 분류 심화

### 학습 내용
- 합성곱 신경망(CNN) 구현
- CNN 구조 및 동작 원리
- 말과 사람 이미지 분류
- `image_dataset_from_directory()` 사용법
- 학습/검증 데이터 분리
- 이미지 증식(Image Augmentation)
- 전이 학습(Transfer Learning)
- 다중 분류(Multi-class Classification)
- Dropout을 이용한 과적합 방지

---

# 학습 목표

- TensorFlow와 Keras 기본 사용법 익히기
- 딥러닝 모델 생성 및 학습 과정 이해
- 이미지 분류 모델 구현
- CNN의 구조와 동작 원리 학습
- 과적합 방지 기법(Early Stopping, Dropout) 이해
- 이미지 증식과 전이 학습 활용

---

# 사용 기술

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Google Colab

---

# 실행 환경

- Python 3.x
- TensorFlow 2.x
- Google Colab 또는 Jupyter Notebook

---

# 실행 방법

1. 필요한 라이브러리를 설치합니다.

```bash
pip install tensorflow matplotlib numpy
```

2. Jupyter Notebook 또는 Google Colab에서 원하는 `.ipynb` 파일을 실행합니다.

3. 셀을 순서대로 실행하여 모델 학습과 결과를 확인합니다.

---

# 학습 순서

1. TensorFlow 기초
2. Fashion MNIST 이미지 분류
3. CNN 구현
4. 이미지 증식
5. 전이 학습
6. 다중 분류
7. Dropout을 이용한 성능 개선