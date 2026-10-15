import cv2

# (Windows) Read from the first camera device
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# (Mac) Read from the first camera device
# cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

topLeft = (50, 150)
font_size = 1.0
bold = 0

r_val = 255
g_val = 255
b_val = 0

# Callback function for the trackbar
def on_font_size_trackbar(value):
    global font_size
    font_size = max(0.2, value / 10.0)

def on_bold_trackbar(value):
    global bold
    bold = value

def on_r_trackbar(value):
    global r_val
    r_val = value

def on_g_trackbar(value):
    global g_val
    g_val = value

def on_b_trackbar(value):
    global b_val
    b_val = value

cv2.namedWindow("Camera")
cv2.createTrackbar("font size (x0.1)", "Camera", 10, 50, on_font_size_trackbar)
cv2.createTrackbar("bold", "Camera", bold, 10, on_bold_trackbar)

cv2.createTrackbar("R", "Camera", r_val, 255, on_r_trackbar)
cv2.createTrackbar("G", "Camera", g_val, 255, on_g_trackbar)
cv2.createTrackbar("B", "Camera", b_val, 255, on_b_trackbar)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Text
    text_color = (b_val, g_val, r_val)
    cv2.putText(frame, "TEXT",
        topLeft, cv2.FONT_HERSHEY_SIMPLEX, font_size, text_color, 1 + bold)

    # Display
    cv2.imshow("Camera",frame)

    # 1 ms 동안 대기하며 키 입력을 받고 'q' 입력 시 종료
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()