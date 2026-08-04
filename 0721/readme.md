# Ubuntu 가상환경 및 Python(uv / Conda) 개발환경 구축 가이드

> Windows(VS Code), Ubuntu(OSBoxes), Python(uv), Conda, JupyterLab 환경을 한 번에 구성하는 실습용 정리입니다.

---

# 목차

1. Windows PowerShell 설정
2. uv(Python) 개발환경 구성 (VS Code)
3. Conda 개발환경 구성
4. Ubuntu(OSBoxes) 초기 설정
5. SSH 서버 구축
6. Apache 웹 서버 구축
7. 고정 IP 설정(Netplan)
8. uv(Python) 개발환경 구성 (Ubuntu)
9. vi Editor 기본 사용법
10. 자주 사용하는 명령어

---

# 1. Windows PowerShell 설정

## PowerShell 실행 정책 변경

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

설명

- PowerShell 스크립트 실행 허용
- 현재 사용자만 적용

---

## uv PATH 등록

```powershell
$Env:Path += "C:\Users\user\.local\bin"
```

설치 위치

```
C:\Users\user\.local\bin
```

확인

```powershell
uv
```

또는

```powershell
uv --version
```

---

# 2. VS Code에서 uv(Python) 개발환경 구성

## 프로젝트 생성

```powershell
uv init --python 3.12 py312
```

생성되는 파일

```
py312
│
├── pyproject.toml
├── main.py
├── .python-version
```

프로젝트 이동

```powershell
cd py312
```

---

## 가상환경 생성

```powershell
uv venv
```

예시

```
Using CPython 3.12.13
Creating virtual environment at: .venv
```

---

## 가상환경 활성화

```powershell
.venv\Scripts\activate
```

예시

```
(py312) PS D:\intel\py312>
```

---

## 패키지 설치

```powershell
uv add jupyterlab ipykernel numpy pandas matplotlib
```

설치 패키지

|패키지|설명|
|-------|----------------|
|jupyterlab|JupyterLab|
|ipykernel|Python Kernel|
|numpy|수치 계산|
|pandas|데이터 분석|
|matplotlib|그래프|

---

## Python 실행

```powershell
uv run main.py
```

---

## 설치된 패키지 확인

```powershell
uv pip list
```

---

## Python 버전 확인

```powershell
uv python list
```

---

# 전체 실행 순서 (VS Code)

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

$Env:Path += "C:\Users\user\.local\bin"

uv init --python 3.12 py312

cd py312

uv venv

.venv\Scripts\activate

uv add jupyterlab ipykernel numpy pandas matplotlib

uv run main.py
```

---

# 3. Conda 개발환경 구성

## 환경 생성

```powershell
conda create -n con312 python=3.12
```

---

## 환경 활성화

```powershell
conda activate con312
```

---

## Jupyter 설치

```powershell
conda install jupyter notebook
```

또는

```powershell
conda install jupyterlab
```

---

## 환경 확인

```powershell
conda info --envs
```

---

## Jupyter 실행

```powershell
jupyter lab --notebook-dir=D:\intel\pyeqw\jupytercon
```

---

# 4. Ubuntu(OSBoxes) 초기 설정

비밀번호 변경

```bash
passwd
```

Root 비밀번호 설정

```bash
sudo passwd root
```

Root 로그인

```bash
su - root
```

---

패키지 업데이트

```bash
sudo apt update

sudo apt upgrade
```

필요 시 재부팅

```bash
sudo reboot
```

---

# 5. SSH 서버 구축

설치

```bash
sudo apt install openssh-server
```

상태 확인

```bash
sudo systemctl status ssh
```

시작

```bash
sudo systemctl start ssh
```

부팅 시 자동 실행

```bash
sudo systemctl enable ssh
```

IP 확인

```bash
ip a
```

원격 접속(Windows)

```powershell
ssh 사용자명@IP주소
```

예시

```powershell
ssh osboxes@192.168.100.50
```

---

# 6. Apache 웹 서버 구축

설치

```bash
sudo apt install apache2
```

상태 확인

```bash
sudo systemctl status apache2
```

시작

```bash
sudo systemctl start apache2
```

자동 시작

```bash
sudo systemctl enable apache2
```

웹 문서 복사

```bash
sudo cp second.html /var/www/html
```

파일 소유권 변경

```bash
sudo chown osboxes:osboxes test.html
```

웹 브라우저에서 확인

```
http://IP주소
```

예시

```
http://192.168.100.50
```

---

# 7. Ubuntu 고정 IP 설정(Netplan)

설정 파일 이동

```bash
cd /etc/netplan
```

설정 파일 수정

```bash
sudo vi 50-cloud-init.yaml
```

예시

```yaml
network:
  version: 2
  renderer: networkd

  ethernets:
    enp0s3:
      dhcp4: no
      addresses:
        - 192.168.100.50/24
      routes:
        - to: default
          via: 192.168.100.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 1.1.1.1
```

적용

```bash
sudo netplan apply
```

확인

```bash
ip a
```

---

# 8. Ubuntu에서 uv(Python) 개발환경 구성

curl 설치

```bash
sudo apt install curl
```

uv 설치

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

환경 적용

```bash
source $HOME/.local/bin/env
```

프로젝트 생성

```bash
uv init pyprj --python=3.12
```

Python 목록 확인

```bash
uv python list
```

Python 설치

```bash
uv python install 3.12
```

가상환경 생성

```bash
uv venv --python=3.12
```

가상환경 활성화

```bash
source .venv/bin/activate
```

패키지 설치

```bash
uv add ipykernel jupyterlab numpy pandas matplotlib
```

실행

```bash
uv run main.py
```

---

# 9. vi Editor 기본 사용법

## 입력 모드

```
i
```

현재 위치 입력

```
a
```

현재 문자 뒤 입력

```
o
```

아래 줄 생성

```
O
```

위 줄 생성

---

## 삭제

```
x
```

한 글자 삭제

```
dd
```

한 줄 삭제

---

## 복사 / 붙여넣기

```
yy
```

한 줄 복사

```
p
```

붙여넣기

---

## 이동

```
h
j
k
l
```

← ↓ ↑ →

마지막 줄

```
G
```

특정 줄 이동

```
:3
```

---

## 라인 번호

표시

```
:set number
```

숨기기

```
:set nonumber
```

---

## 저장

저장

```
:w
```

저장 후 종료

```
:wq
```

종료

```
:q
```

강제 종료

```
:q!
```

---

# 10. 자주 사용하는 Linux 명령어

현재 위치

```bash
pwd
```

파일 목록

```bash
ls
```

상세 목록

```bash
ls -al
```

폴더 이동

```bash
cd
```

상위 폴더

```bash
cd ..
```

폴더 생성

```bash
mkdir 폴더명
```

파일 삭제

```bash
rm 파일명
```

폴더 삭제

```bash
rm -r 폴더명
```

파일 복사

```bash
cp 원본 대상
```

파일 이동

```bash
mv 원본 대상
```

현재 IP 확인

```bash
ip a
```

---

# 실습 순서 요약

1. Windows PowerShell 설정
2. VS Code에서 uv 개발환경 구축
3. Conda 개발환경 구축
4. Ubuntu 초기 설정
5. SSH 서버 설치 및 원격 접속
6. Apache 웹 서버 설치
7. Netplan으로 고정 IP 설정
8. Ubuntu에서 uv + Python + JupyterLab 개발환경 구축
9. vi Editor 사용법 익히기
10. VS Code Remote SSH를 이용하여 Ubuntu 원격 개발 환경 연결

---

# 참고

- **uv** : 빠른 Python 패키지 및 가상환경 관리자
- **Conda** : Python 및 데이터 과학용 패키지/환경 관리자
- **JupyterLab** : 웹 기반 Python 개발 환경
- **SSH** : 원격 접속 프로토콜
- **Apache2** : 웹 서버
- **Netplan** : Ubuntu 네트워크 설정 도구
- **VS Code Remote SSH** : VS Code에서 Ubuntu 서버에 원격 접속하여 개발할 수 있는 확장 기능
