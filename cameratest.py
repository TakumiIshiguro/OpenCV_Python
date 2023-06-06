import cv2

cap = cv2.VideoCapture(0)  # カメラデバイスのインデックスを指定（0はデフォルトのカメラ）

while True:
    ret, frame = cap.read()  # ビデオフレームの読み込み

    # カメラからの映像を表示する処理
    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' キーを押したらループを終了
        break

cap.release()  # カメラリリース
cv2.destroyAllWindows()  # ウィンドウを閉じる

