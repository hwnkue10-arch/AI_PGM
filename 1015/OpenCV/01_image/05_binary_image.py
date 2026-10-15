from pathlib import Path
import cv2

RESOURCE_PATH = Path(__file__).resolve().parent.parent / "resources"
image = cv2.imread(RESOURCE_PATH / "text.png", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
#                         │     │    │         │
#                         │     │    │         └─ 이진화 방식 (THRESH_BINARY)
#                         │     │    └─ maxval: 조건을 만족할 때 부여할 최댓값
#                         │     └─ thresh: 기준이 되는 임계값(Threshold)
#                         └─ src: 입력 이미지 (단일 채널 GrayScale)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()