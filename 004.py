import cv2    # 練習調整 HSV 閾值篩選顏色(影像版)
import numpy as np

def empty(a):
    pass

# 開啟攝影機 (0 代表預設攝影機，如果有多個可以改成 1、2 ...)
cap = cv2.VideoCapture(0)

# 建立 HSV 調整視窗
cv2.namedWindow('trackBar')
cv2.resizeWindow('trackBar', 640, 480)
cv2.createTrackbar('Hue min', 'trackBar', 0, 179, empty)
cv2.createTrackbar('Hue max', 'trackBar', 179, 179, empty)
cv2.createTrackbar('Sat min', 'trackBar', 0, 255, empty)
cv2.createTrackbar('Sat max', 'trackBar', 255, 255, empty)
cv2.createTrackbar('Val min', 'trackBar', 0, 255, empty)
cv2.createTrackbar('Val max', 'trackBar', 255, 255, empty)

while True:
    success, img = cap.read()
    if not success:
        print("無法讀取攝影機影像")
        break

    # BGR 轉 HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 讀取滑桿數值
    h_min = cv2.getTrackbarPos('Hue min', 'trackBar')
    h_max = cv2.getTrackbarPos('Hue max', 'trackBar')
    s_min = cv2.getTrackbarPos('Sat min', 'trackBar')
    s_max = cv2.getTrackbarPos('Sat max', 'trackBar')
    v_min = cv2.getTrackbarPos('Val min', 'trackBar')
    v_max = cv2.getTrackbarPos('Val max', 'trackBar')

    # 設定 HSV 範圍
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # 篩選顏色
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    # 顯示結果
    cv2.imshow("Original", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    # 按 q 離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
