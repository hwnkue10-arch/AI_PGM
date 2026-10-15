from pathlib import Path
import cv2

IMG_PATH = Path(__file__).resolve().parent.parent / "resources"
image = cv2.imread(IMG_PATH / "jang.jpg", cv2.IMREAD_COLOR)
image2 = cv2.imread(IMG_PATH / "or_layer.png", cv2.IMREAD_COLOR)
mask = cv2.imread(IMG_PATH / "layer.png", cv2.IMREAD_GRAYSCALE)

dst = cv2.bitwise_and(image, image2, mask=mask)

cv2.imshow("src", image)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
