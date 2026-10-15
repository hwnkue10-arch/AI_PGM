from pathlib import Path
from datetime import datetime as dt
import cv2

# Read from the recorded video file
RESOURCE_PATH = Path(__file__).resolve().parent.parent / "resources"
CAPTURE_PATH = Path(__file__).resolve().parent.parent / "resources" / "capture"
RECORDING_PATH = Path(__file__).resolve().parent.parent / "resources" / "recording"

cap = cv2.VideoCapture(RESOURCE_PATH / "movie.mp4")
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps) if fps > 0 else 33
is_video_recording = False

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
    now = str(dt.now().strftime("%d-%H-%M-%s"))

    if key & 0xFF == ord("q"):
        break
    elif key & 0xFF == ord("c"):
        cv2.imwrite(str(CAPTURE_PATH) + "/" + now + ".png", resized_frame)
    elif key & 0xFF == ord("r") and not is_video_recording:
        is_video_recording = True
        h, w = resized_frame.shape[:2]
        video_recording = cv2.VideoWriter(str(RECORDING_PATH) + "/" + now + ".mp4", fourcc, 20.0, (w, h))

# 3. 비디오 라이터가 정상적으로 열렸는지 즉시 확인
        if not video_recording.isOpened():
            print("[Error] VideoWriter 초기화 실패! 코덱이나 경로를 확인하세요.")
            video_recording = None

    elif key & 0xFF == ord("s") and is_video_recording:
        is_video_recording = False
        video_recording.release()

    if is_video_recording == True:
        video_recording.write(resized_frame)

cap.release()
cv2.destroyAllWindows()
