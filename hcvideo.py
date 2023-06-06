import cv2
import numpy as np

# カメラのキャプチャを開始
cap = cv2.VideoCapture(0)

while True:
    # フレームを1つずつ読み込む
    ret, frame = cap.read()

    # フレームが正常に読み込まれなかった場合は終了する
    if not ret:
        break

    # フレームをグレースケールに変換する
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 平滑化
    gaus = cv2.GaussianBlur(gray, (33, 33), sigmaX=3)
  
    # 円を検出
    circles = cv2.HoughCircles(gaus, cv2.HOUGH_GRADIENT, 1, 250, param1=100, param2=25, minRadius=50, maxRadius=100)
    
    # 検出した円が存在する場合にのみ描画する
    if circles is not None:
        circles = np.uint16(np.around(circles))
        
        # 検出した円を画像に描き、ファイルを書き出す
        for i in circles[0,:]:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)

    # グレースケール画像を表示する
    cv2.imshow('hcvideo', frame)

    # 'q'キーを押すとループを抜ける
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# キャプチャを解放し、ウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()

