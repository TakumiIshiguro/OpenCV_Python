import cv2
import numpy as np

# 画像を読み込み、グレースケールに変換
img = cv2.imread('IMG_5862.jpg', cv2.IMREAD_GRAYSCALE)

# 平滑化
gaimg = cv2.GaussianBlur(img, (33, 33), sigmaX=3)

# 円を検出
circles = cv2.HoughCircles(gaimg, cv2.HOUGH_GRADIENT, 1, 250, param1=100, param2=25, minRadius=50, maxRadius=100)
circles = np.uint16(np.around(circles))

# 検出した円を画像に描き、ファイルを書き出しする
for i in circles[0,:]:
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imwrite('gaimg.jpg', gaimg)
cv2.imwrite('detected-circles.jpg', img)

