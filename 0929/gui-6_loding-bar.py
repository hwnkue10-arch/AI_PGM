from tkinter import *
from tkinter import ttk

# 창 생성
win = Tk()
win.geometry("400x250")
win.title("로딩 및 프로그레스바 예제")

# 상태 변수 설정
is_running = False  # 진행 상태 확인용
current_progress = 0  # 현재 진행률

# 프로그레스바 생성 (최대값 100)
progress = ttk.Progressbar(win, maximum=100, length=300, mode="determinate")
progress.pack(pady=30)

# 상태 표시 레이블
status_label = Label(win, text="대기 중...", font=("Arial", 11))
status_label.pack(pady=10)

# 프로그레스바를 증가시키는 함수
def update_progress():
    global current_progress, is_running
    
    # 실행 중이고 진행률이 100 미만일 때만 작동
    if is_running and current_progress < 100:
        current_progress += 1
        progress['value'] = current_progress
        status_label.config(text=f"로딩 중... {current_progress}%")
        
        # 0.05초(50밀리초) 뒤에 다시 함수 호출
        win.after(50, update_progress)
        
    elif current_progress >= 100:
        is_running = False
        status_label.config(text="진행 완료!")
        start_btn.config(state="normal") # 완료 후 시작 버튼 활성화

# 시작 버튼 클릭 함수
def start_loading():
    global is_running, current_progress
    
    if not is_running:
        # 이미 완료된 상태(100%)였다면 0부터 다시 시작하도록 초기화
        if current_progress >= 100:
            current_progress = 0
            progress['value'] = 0
            
        is_running = True
        start_btn.config(state="disabled") # 실행 중에는 시작 버튼 비활성화
        update_progress()

# 일시정지 버튼 클릭 함수
def pause_loading():
    global is_running
    # 로딩이 진행 중일 때만 일시정지 작동
    if is_running:
        is_running = False
        start_btn.config(state="normal") # 일시정지 시 시작 버튼 다시 활성화
        status_label.config(text=f"일시정지됨 ({current_progress}%)")

# 버튼 배치 프레임
btn_frame = Frame(win)
btn_frame.pack(pady=10)

start_btn = Button(btn_frame, text="시작", width=10, command=start_loading)
start_btn.grid(row=0, column=0, padx=5)

pause_btn = Button(btn_frame, text="일시정지", width=10, command=pause_loading)
pause_btn.grid(row=0, column=1, padx=5)

win.mainloop()