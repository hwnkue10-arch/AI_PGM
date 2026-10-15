from pathlib import Path
import cv2

# 이미지 파일을 Read
RESOURCE_PATH = Path(__file__).resolve().parent.parent / "resources"
img = cv2.imread(RESOURCE_PATH / "jang.jpg", cv2.IMREAD_COLOR)

# Image 란 이름의 Display 창 생성
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
# cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)

# Numpy ndarray H/W/C order
print(img.shape)

# Read 한 이미지 파일을 Display
cv2.imshow("image", img)

# 별도 키 입력이 있을때 까지 대기
key = cv2.waitKey(0)

if key == ord("s"):
    # output.png 로 읽은 이미지 파일을 저장
    cv2.imwrite("output.png", img)

# Destroy all windows
cv2.destroyAllWindows()
