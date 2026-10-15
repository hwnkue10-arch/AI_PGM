"""
00_python_basics/01_env_and_syntax.py
OpenCV 실습을 위한 파이썬 가상환경 검증 및 핵심 기초 문법 인벤토리
"""
import sys
from pathlib import Path

# 1. 가상환경 및 패키지 설치 검증
print(f"[Python Executable] {sys.executable}")
print(f"[Python Version] {sys.version}")

# 2. ord / chr 함수 및 비트 마스킹 (& 0xFF)
key_char = "s"
ascii_val = ord(key_char)          # 115
recovered_char = chr(ascii_val)    # 's'
bitmasked_key = 115 & 0xFF         # 115 (32비트 반환값을 8비트로 마스킹)
print(f"[ord/chr] char: '{key_char}' -> ascii: {ascii_val} -> chr: '{recovered_char}', masked: {bitmasked_key}")

# 3. pathlib.Path 활용 리소스 경로 탐색
ROOT_DIR = Path(__file__).resolve().parent.parent
RESOURCE_DIR = ROOT_DIR / "resources"
print(f"[Pathlib] Root: {ROOT_DIR}, Resource: {RESOURCE_DIR} (Exists: {RESOURCE_DIR.exists()})")

# 4. 전역 변수(global) 스코프 제어
counter = 0

def increment_counter():
    global counter
    counter += 1

increment_counter()
print(f"[Global Scope] Counter after call: {counter}")

# 5. NumPy 2D/3D 배열 슬라이싱 (배열 형태 시뮬레이션)
# 행(Y) 슬라이싱 후 열(X) 슬라이싱
grid = [[f"({r},{c})" for c in range(5)] for r in range(5)]
# grid[1:3][2:4] 형태의 2차원 범위 선택 원리
print(f"[Slicing Concept] Grid 5x5 initialized.")
