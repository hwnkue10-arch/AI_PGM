# Tkinter GUI 예제 모음 설명서

이 문서는 파이썬의 표준 GUI 라이브러리인 Tkinter의 핵심 위젯(Text, Entry, Label, Checkbutton, Progressbar) 사용법을 다룬 4개 예제 스크립트의 기능과 동작 구조를 정리한 설명서입니다[cite: 6, 7, 8, 9].

---

## 1. `gui-2.py` (텍스트 입력 및 엔트리 위젯)

* **목적**: 여러 줄 입력 위젯(`Text`)과 한 줄 입력 위젯(`Entry`)의 생성, 기본값 삽입, 데이터 추출 방식의 차이를 확인합니다[cite: 6].
* **주요 구성 요소**:
  * `win.geometry("400x400")`: 400×400 해상도의 기본 윈도우 생성[cite: 6].
  * `txt = Text(win, width=30, height=5)`: 여러 줄을 입력할 수 있는 텍스트 영역을 생성하고 `"1.0"`(1번째 줄 0번째 문자) 위치에 기본 안내 문구를 삽입합니다[cite: 6].
  * `e = Entry(win, width=30)`: 1줄 전용 입력 필드를 생성하고 `0` 인덱스에 기본 텍스트를 삽입합니다[cite: 6].
  * `btncmd()`: 버튼 클릭 시 호출되는 함수입니다[cite: 6].
    * `txt.get("1.0", END)`: 텍스트 위젯의 첫 번째 줄부터 끝까지의 모든 텍스트를 가져와 콘솔에 출력합니다[cite: 6].
    * `e.get()[0:0]`: 엔트리의 텍스트를 가져오지만 슬라이싱 범위가 `[0:0]`이므로 빈 문자열을 반환합니다 (전체 출력을 위해서는 `e.get()` 사용 필요)[cite: 6].

---

## 2. `gui-4_lable.py` (레이블 위젯 및 배치)

* **목적**: 윈도우 화면에 정적 텍스트를 출력하는 `Label` 위젯의 기본 사용법과 하단 정렬 배치 방식을 확인합니다[cite: 7].
* **주요 구성 요소**:
  * `label1 = Label(win, text="Good")`: "Good"이라는 문자열을 표시하는 텍스트 레이블을 생성합니다[cite: 7].
  * `label1.pack(side="bottom")`: `pack()` 배치 관리자의 `side` 옵션을 사용하여 레이블을 윈도우 창의 맨 아래쪽에 정렬하여 배치합니다[cite: 7].

---

## 3. `gui-5.py` (체크버튼 위젯 및 상태 제어)

* **목적**: 참/거짓(Boolean) 상태를 갖는 `Checkbutton` 위젯을 만들고, 전용 변수(`BooleanVar`)와 연동하여 사용자의 선택 상태를 읽어옵니다[cite: 8].
* **주요 구성 요소**:
  * `chkvar = BooleanVar()`: 체크박스의 체크 여부를 Boolean(`True`/`False`) 타입으로 추적하는 Tkinter 전용 상태 변수입니다[cite: 8].
  * `chkbox = Checkbutton(win, text="don't show for today", variable=chkvar)`: 레이블 텍스트와 함께 `chkvar` 변수를 바인딩하여 체크/해제 시 값이 자동 변경되도록 설정합니다[cite: 8].
  * `btncmd()`: "click" 버튼을 누르면 `chkvar.get()`을 실행하여 체크 상태(체크 시 `True`, 해제 시 `False`)를 콘솔에 출력합니다[cite: 8].

---

## 4. `gui-6_loding-bar.py` (프로그레스바 및 비동기 타이머 로딩)

* **목적**: `ttk.Progressbar`와 Tkinter의 타이머 스케줄러(`win.after`)를 활용하여 프로그램이 멈추지 않고 단계적으로 증가하는 로딩/진행률 바와 시작·일시정지 제어를 구현합니다[cite: 9].
* **주요 구성 요소**:
  * `progress = ttk.Progressbar(..., maximum=100, length=300, mode="determinate")`: 0부터 100까지 정량적인 수치(`determinate`)로 진행도를 나타내는 가로 300px 크기의 프로그레스바입니다[cite: 9].
  * `status_label`: 현재 진행 상태 텍스트("대기 중...", "로딩 중... X%", "진행 완료!", "일시정지됨")를 실시간으로 갱신하는 레이블입니다[cite: 9].
  * **핵심 함수**:
    * `update_progress()`: `is_running`이 참일 때 진행률(`current_progress`)을 1씩 올린 뒤, `win.after(50, update_progress)`를 통해 50밀리초(0.05초) 간격으로 자기 자신을 반복 호출하며 게이지를 채웁니다[cite: 9].
    * `start_loading()`: 진행 상태를 켜고(`is_running = True`), 중복 실행을 막기 위해 시작 버튼을 비활성화(`state="disabled"`)한 후 프로그레스바 갱신 루프를 시작합니다 (100% 도달 후 재시작 시 0%로 자동 리셋)[cite: 9].
    * `pause_loading()`: `is_running = False`로 설정하여 다음 타이머 호출을 차단하고 로딩을 일시 중지하며 시작 버튼을 다시 활성화합니다[cite: 9].