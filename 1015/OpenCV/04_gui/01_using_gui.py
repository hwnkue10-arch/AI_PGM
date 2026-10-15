import cv2

# (Windows) Read from the first camera device
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# (Mac) Read from the first camera device
# cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

topLeft = (50, 50)
bottomRight = (300, 300)
clicked_points = []

# 1. 마우스 이벤트 콜백 함수 정의
def on_mouse(event, x, y, flags, param):
    # 마우스 왼쪽 버튼 클릭 시
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))

cv2.namedWindow("Camera")
cv2.setMouseCallback("Camera", on_mouse)

# 성공적으로 video device 가 열렸으면 while 문 반복
while(cap.isOpened()):
    # 한 프레임을 읽어옴
    ret, frame = cap.read()

    # Line
    cv2.line(frame, topLeft, bottomRight, (0, 255, 0), 5)

    # Rectangle
    cv2.rectangle(frame,
        [pt+30 for pt in topLeft], [pt-30 for pt in bottomRight], (0, 0, 255), 5)

    circle_center = (175, 175)
    cv2.circle(frame, circle_center, 60, (255, 0, 0), 10)

    # Text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "me",
        [pt+80 for pt in topLeft], font, 2, (0, 255, 255), 10)

    for pt in clicked_points:
        # cv2.circle(이미지, 중심좌표, 반지름, BGR색상, 선두께)
        cv2.circle(frame, pt, 20, (0, 0, 255), -1)

    # Display
    cv2.imshow("Camera",frame)

    # 1 ms 동안 대기하며 키 입력을 받고 'q' 입력 시 종료
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()