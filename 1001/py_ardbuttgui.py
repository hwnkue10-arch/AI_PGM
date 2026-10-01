import serial
import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk, messagebox
import ctypes

# 윈도우 고해상도 안티에일리어싱 적용
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

class LedControlApp:
    # 아두이노 if문과 1:1 매칭되는 단일 문자 프로토콜 설정 ('A', 'B', 'C')
    COMMANDS = [
        {"id": "A", "label": "켜기 (ON)", "color": "#059669", "hover": "#10b981"},
        {"id": "B", "label": "끄기 (OFF)", "color": "#272a34", "hover": "#353946"},
        {"id": "C", "label": "점멸 (BLINK)", "color": "#d97706", "hover": "#f59e0b"}
    ]

    def __init__(self, root):
        self.root = root
        self.root.title("LED Controller")
        self.root.geometry("380x380")
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

        self.root.option_add("*TCombobox*Listbox.background", "#1c1f26")
        self.root.option_add("*TCombobox*Listbox.foreground", "#ffffff")
        self.root.option_add("*TCombobox*Listbox.selectBackground", "#2563eb")
        self.root.option_add("*TCombobox*Listbox.selectForeground", "#ffffff")
        self.root.option_add("*TCombobox*Listbox.font", ("Malgun Gothic", 9))

    def build_ui(self):
        # 1. 미니멀 헤더
        header = tk.Frame(self.root, bg="#111215", height=42)
        header.pack(fill="x", padx=20, pady=(18, 6))
        header.pack_propagate(False)

        tk.Label(
            header, text="Mode Controller",
            font=("Malgun Gothic", 12, "bold"),
            fg="#e5e7eb", bg="#111215"
        ).pack(side="left", anchor="center")

        # 2. 포트 설정 카드
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

        # 3. LED 제어 카드
        mode_card = tk.Frame(self.root, bg="#181a20", highlightthickness=1, highlightbackground="#272a34", padx=14, pady=12, height=130)
        mode_card.pack(fill="x", padx=18, pady=6)
        mode_card.pack_propagate(False)

        mode_top = tk.Frame(mode_card, bg="#181a20")
        mode_top.pack(fill="x", pady=(0, 12))

        tk.Label(mode_top, text="동작 모드 제어 (Pin 11)", font=("Malgun Gothic", 10, "bold"), fg="#f3f4f6", bg="#181a20").pack(side="left")

        # 뱃지 가로 너비 확장 (width=14로 늘려 글자 잘림 방지)
        self.mode_badge = tk.Label(mode_top, text="READY", font=("Consolas", 8, "bold"), width=14, fg="#9ca3af", bg="#272a34")
        self.mode_badge.pack(side="right")

        # 3버튼 균등 배치
        btn_grid = tk.Frame(mode_card, bg="#181a20")
        btn_grid.pack(fill="x")

        for idx, cmd in enumerate(self.COMMANDS):
            b = tk.Button(
                btn_grid, text=cmd["label"], font=("Malgun Gothic", 9, "bold"),
                bg=cmd["color"], fg="#ffffff" if cmd["id"] != "B" else "#9ca3af",
                activebackground=cmd["hover"], activeforeground="#ffffff",
                relief="flat", bd=0, cursor="hand2",
                command=lambda c=cmd["id"]: self.send_command(c)
            )
            padx_val = (0, 4) if idx < len(self.COMMANDS) - 1 else (0, 0)
            b.pack(side="left", fill="x", expand=True, padx=padx_val, ipady=5)

            b.bind("<Enter>", lambda e, btn=b, col=cmd["hover"]: btn.config(bg=col, fg="#ffffff"))
            b.bind("<Leave>", lambda e, btn=b, col=cmd["color"], cid=cmd["id"]: btn.config(bg=col, fg="#ffffff" if cid != "B" else "#9ca3af"))

        # 4. 하단 상태 바
        self.footer = tk.Label(
            self.root, text="포트 미연결", font=("Malgun Gothic", 8),
            fg="#6b7280", bg="#111215", pady=12
        )
        self.footer.pack(side="bottom")

    def scan_ports(self):
        self.port_map.clear()
        detected_ports = []
        arduino_recommended = None

        for p in serial.tools.list_ports.comports():
            desc = p.description.strip()
            hwid = p.hwid.upper()

            if p.device in ["COM1", "COM2"] and ("통신" in desc or "Communications" in desc):
                continue

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
        self.mode_badge.config(text="READY", fg="#9ca3af", bg="#272a34")

    def send_command(self, char_cmd):
        if not self.ser or not self.ser.is_open:
            messagebox.showinfo("안내", "아두이노 포트를 먼저 연결해 주세요.")
            return

        try:
            # 아두이노가 읽을 수 있도록 단일 바이트('A', 'B', 'C') 전송
            self.ser.write(char_cmd.encode())

            # 뱃지 텍스트를 간결하고 명확하게 변경 (잘림 방지)
            if char_cmd == "A":
                self.mode_badge.config(text="ACTIVE: ON", fg="#34d399", bg="#0f291e")
            elif char_cmd == "B":
                self.mode_badge.config(text="INACTIVE: OFF", fg="#f87171", bg="#2c1619")
            elif char_cmd == "C":
                self.mode_badge.config(text="BLINKING", fg="#fbbf24", bg="#31220a")
        except Exception as e:
            messagebox.showerror("전송 실패", str(e))


if __name__ == "__main__":
    app_root = tk.Tk()
    app = LedControlApp(app_root)
    app_root.mainloop()