from pathlib import Path
import cv2

RESOURCE_PATH = Path(__file__).resolve().parent.parent / "resources"
image = cv2.imread(RESOURCE_PATH / "jang.jpg", cv2.IMREAD_COLOR)

dst = cv2.blur(image, (10, 10), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)

cv2.imshow("src", image)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
