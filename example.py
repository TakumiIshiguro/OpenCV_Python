import cv2

# 画像の読み込み
image = cv2.imread('IMG_1.jpg')

# 画像の表示
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.waitKey(0)

cv2.destroyAllWindows()

