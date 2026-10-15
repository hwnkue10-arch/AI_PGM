from pathlib import Path
import cv2

RESOURCE_PATH = Path(__file__).resolve().parent.parent / "resources"
image = cv2.imread(RESOURCE_PATH / "jang.jpg", cv2.IMREAD_COLOR)

b, g, r = cv2.split(image)

# Numpy
# b = image[:, :, 0]
# g = image[:, :, 1]
# r = image[:, :, 2]
inverse = cv2.merge((r, g, b))

cv2.imshow("B", b)
cv2.imshow("G", g)
cv2.imshow("R", r)
cv2.imshow("inverse", inverse)
cv2.waitKey()
cv2.destroyAllWindows()