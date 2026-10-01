import serial
import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk, messagebox
import ctypes

# 윈도우 글자/테두리 폰트 렌더링을 선명하고 부드럽게 설정 (안티에일리어싱 활성화)
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

class ArduinoMinimalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LED Controller")
        self.root.geometry("350x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#111215")

        self.ser = None
        self.selected_port_str = tk.StringVar()
        self.port_map = {}

        self.setup_styles()
        self.build_ui()
        self.scan_ports()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')

        # 콤보박스 색상 대비 완전 분리 (어두운 배경 + 뚜렷한 흰색 글씨)
        style.configure(
            "Clean.TCombobox",
            fieldbackground="#1c1f26",
            background="#252932",
            foreground="#f3f4f6",
            darkcolor="#1c1f26",
            lightcolor="#1c1f26",
            bordercolor="#2f3441",
            arrowcolor="#9ca3af",
            padding=5
        )
        style.map(
            "Clean.TCombobox",
            fieldbackground=[("readonly", "#1c1f26")],
            foreground=[("readonly", "#ffffff")],
            selectbackground=[("readonly", "#1c1f26")],
            selectforeground=[("readonly", "#ffffff")]
        )

        # 펼쳐지는 드롭다운 리스트 팝업 색상 설정
        self.root.option_add("*TCombobox*Listbox.background", "#1c1f26")
        self.root.option_add("*TCombobox*Listbox.foreground", "#ffffff")
        self.root.option_add("*TCombobox*Listbox.selectBackground", "#3b82f6")
        self.root.option_add("*TCombobox*Listbox.selectForeground", "#ffffff")
        self.root.option_add("*TCombobox*Listbox.font", ("Malgun Gothic", 9))

    def build_ui(self):
        # 1. 미니멀 헤더
        header = tk.Frame(self.root, bg="#111215", height=42)
        header.pack(fill="x", padx=20, pady=(18, 6))
        header.pack_propagate(False)

        tk.Label(
            header, text="Device Control",
            font=("Malgun Gothic", 12, "bold"),
            fg="#e5e7eb", bg="#111215"
        ).pack(side="left", anchor="center")

        # 2. 포트 카드 컨테이너 (은은한 테두리 패딩 기법)
        port_card = tk.Frame(self.root, bg="#181a20", highlightthickness=1, highlightbackground="#272a34", padx=14, pady=12)
        port_card.pack(fill="x", padx=18, pady=6)

        port_top = tk.Frame(port_card, bg="#181a20")
        port_top.pack(fill="x", pady=(0, 8))
        tk.Label(port_top, text="연결 포트", font=("Malgun Gothic", 9, "bold"), fg="#9ca3af", bg="#181a20").pack(side="left")

        port_ctrl = tk.Frame(port_card, bg="#181a20")
        port_ctrl.pack(fill="x")

        self.cb_ports = ttk.Combobox(
            port_ctrl, textvariable=self.selected_port_str, state="readonly", 
            style="Clean.TCombobox", font=("Malgun Gothic", 9)
        )
        self.cb_ports.pack(side="left", fill="x", expand=True, padx=(0, 6))

        self.btn_refresh = tk.Button(
            port_ctrl, text="조회", font=("Malgun Gothic", 9),
            bg="#272a34", fg="#e5e7eb", activebackground="#353946", activeforeground="#ffffff",
            relief="flat", bd=0, cursor="hand2", width=5, command=self.scan_ports
        )
        self.btn_refresh.pack(side="left", padx=(0, 4), ipady=3)

        self.btn_connect = tk.Button(
            port_ctrl, text="연결", font=("Malgun Gothic", 9, "bold"),
            bg="#2563eb", fg="#ffffff", activebackground="#1d4ed8", activeforeground="#ffffff",
            relief="flat", bd=0, cursor="hand2", width=6, command=self.toggle_connection
        )
        self.btn_connect.pack(side="left", ipady=3)

        # 3. LED 1 & LED 2 카드
        self.badge_led1 = self.create_device_card(
            title="LED 1 (Pin 11)",
            on_cmd_char='A',
            off_cmd_char='B'
        )

        self.badge_led2 = self.create_device_card(
            title="LED 2 (Pin 12)",
            on_cmd_char='C',
            off_cmd_char='D'
        )

        # 4. 하단 상태 알림
        self.footer = tk.Label(
            self.root, text="포트 미연결", font=("Malgun Gothic", 8),
            fg="#6b7280", bg="#111215", pady=12
        )
        self.footer.pack(side="bottom")

    def create_device_card(self, title, on_cmd_char, off_cmd_char):
        card = tk.Frame(self.root, bg="#181a20", highlightthickness=1, highlightbackground="#272a34", padx=14, pady=12, height=105)
        card.pack(fill="x", padx=18, pady=6)
        card.pack_propagate(False)

        top = tk.Frame(card, bg="#181a20")
        top.pack(fill="x", pady=(0, 10))

        tk.Label(top, text=title, font=("Malgun Gothic", 10, "bold"), fg="#f3f4f6", bg="#181a20").pack(side="left")

        # 고정 폭 뱃지 (상태 변화 시 레이아웃 밀림 방지)
        badge = tk.Label(top, text="OFF", font=("Consolas", 8, "bold"), width=5, fg="#f87171", bg="#2c1619")
        badge.pack(side="right")

        btns = tk.Frame(card, bg="#181a20")
        btns.pack(fill="x")

        # ON 버튼
        b_on = tk.Button(
            btns, text="ON", font=("Malgun Gothic", 9, "bold"),
            bg="#059669", fg="#ffffff", activebackground="#047857", activeforeground="#ffffff",
            relief="flat", bd=0, cursor="hand2",
            command=lambda b=badge, c=on_cmd_char: self.send_cmd(c, b, True)
        )
        b_on.pack(side="left", fill="x", expand=True, padx=(0, 4), ipady=3)
        b_on.bind("<Enter>", lambda e: b_on.config(bg="#10b981"))
        b_on.bind("<Leave>", lambda e: b_on.config(bg="#059669"))

        # OFF 버튼
        b_off = tk.Button(
            btns, text="OFF", font=("Malgun Gothic", 9, "bold"),
            bg="#272a34", fg="#9ca3af", activebackground="#353946", activeforeground="#ffffff",
            relief="flat", bd=0, cursor="hand2",
            command=lambda b=badge, c=off_cmd_char: self.send_cmd(c, b, False)
        )
        b_off.pack(side="right", fill="x", expand=True, padx=(4, 0), ipady=3)
        b_off.bind("<Enter>", lambda e: b_off.config(bg="#353946", fg="#ffffff"))
        b_off.bind("<Leave>", lambda e: b_off.config(bg="#272a34", fg="#9ca3af"))

        return badge

    def scan_ports(self):
        self.port_map.clear()
        detected_ports = []
        arduino_recommended = None

        for p in serial.tools.list_ports.comports():
            desc = p.description.strip()
            hwid = p.hwid.upper()

            # 메인보드 고정 포트(COM1, COM2) 배제
            if p.device in ["COM1", "COM2"] and ("통신" in desc or "Communications" in desc):
                continue

            # 아두이노 장치 식별
            is_arduino = any(k in hwid or k in desc.upper() for k in ["ARDUINO", "CH340", "USB-SERIAL", "CP210", "FT232", "VID:PID=2341"])

            if is_arduino:
                display_name = f"{p.device} (아두이노)"
                if not arduino_recommended:
                    arduino_recommended = display_name
            else:
                display_name = f"{p.device} ({desc.split('(')[0].strip()})"

            self.port_map[display_name] = p.device
            detected_ports.append(display_name)

        if detected_ports:
            self.cb_ports['values'] = detected_ports
            self.selected_port_str.set(arduino_recommended if arduino_recommended else detected_ports[0])
        else:
            self.cb_ports['values'] = ["장치 없음"]
            self.selected_port_str.set("장치 없음")

    def toggle_connection(self):
        if self.ser and self.ser.is_open:
            self.disconnect()
        else:
            self.connect()

    def connect(self):
        selected_text = self.selected_port_str.get()
        actual_port = self.port_map.get(selected_text)

        if not actual_port:
            messagebox.showwarning("경고", "연결 가능한 유효한 포트를 선택하세요.")
            return

        try:
            self.ser = serial.Serial(port=actual_port, baudrate=9600, timeout=1)
            self.btn_connect.config(text="해제", bg="#dc2626", activebackground="#b91c1c")
            self.footer.config(text=f"● 정상 연결: {actual_port}", fg="#10b981")
        except Exception as e:
            messagebox.showerror("오류", f"포트 연결 실패:\n{e}")

    def disconnect(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
        self.ser = None
        self.btn_connect.config(text="연결", bg="#2563eb", activebackground="#1d4ed8")
        self.footer.config(text="포트 미연결", fg="#6b7280")
        self.reset_badges()

    def send_cmd(self, char_cmd, badge_widget, is_on):
        if not self.ser or not self.ser.is_open:
            messagebox.showinfo("안내", "아두이노 연결을 먼저 진행하세요.")
            return
        try:
            self.ser.write(char_cmd.encode())
            if is_on:
                badge_widget.config(text="ON", fg="#34d399", bg="#0f291e")
            else:
                badge_widget.config(text="OFF", fg="#f87171", bg="#2c1619")
        except Exception as e:
            messagebox.showerror("전송 실패", str(e))

    def reset_badges(self):
        if hasattr(self, 'badge_led1') and self.badge_led1:
            self.badge_led1.config(text="OFF", fg="#f87171", bg="#2c1619")
        if hasattr(self, 'badge_led2') and self.badge_led2:
            self.badge_led2.config(text="OFF", fg="#f87171", bg="#2c1619")


if __name__ == "__main__":
    app_root = tk.Tk()
    app = ArduinoMinimalApp(app_root)
    app_root.mainloop()