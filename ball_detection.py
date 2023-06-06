import cv2
import numpy as np

# 画像の読み込み
image = cv2.imread('IMG_1.jpg')

# 黄色の範囲を定義
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([40, 255, 255])

# 画像をHSVに変換
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 黄色の範囲内の領域を抽出
mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

# マスクを使って元の画像から黄色の領域を抽出
yellow_ball = cv2.bitwise_and(image, image, mask=mask)

# 輪郭を検出
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 敷居値を変更する場合はここで調整
threshold = 10

# 輪郭を縁取りする
cv2.drawContours(image, contours, -1, (0, 255, 255), threshold)

# 結果の表示
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

