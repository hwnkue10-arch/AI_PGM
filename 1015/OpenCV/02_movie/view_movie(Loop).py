from pathlib import Path
import cv2

# Read from the recorded video file
RESOURCE_PATH = Path(__file__).resolve().parent.parent / "resources"
cap = cv2.VideoCapture(RESOURCE_PATH / "movie.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps) if fps > 0 else 33

# 동영상 파일이 성공적으로 열렸으면 while 문 반복
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret is False:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Display
    resized_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow("Frame", resized_frame)

    key = cv2.waitKey(delay)
    if key & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
