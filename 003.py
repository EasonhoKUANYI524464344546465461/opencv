import cv2   # 練習調整 HSV 閾值篩選顏色
import numpy as np   # 建立一個矩陣用於色彩篩選

def empty(a):
    pass

img2 = cv2.imread("opencv/002.jpg")
#建立變數儲存圖片 

 #建立視窗
cv2.namedWindow('trackBar')            
#設定視窗大小
cv2.resizeWindow('trackBar', 640, 480)  
#建立六個滑桿用於調整色調
cv2.createTrackbar('Hue min', 'trackBar', 0, 179,empty)     
cv2.createTrackbar('Hue max', 'trackBar', 179, 179,empty)
cv2.createTrackbar('sat min', 'trackBar', 0, 255,empty)
cv2.createTrackbar('sat max', 'trackBar', 255, 255,empty)
cv2.createTrackbar('val min', 'trackBar', 0, 255,empty)
cv2.createTrackbar('val max', 'trackBar', 255, 255,empty)


hsv = cv2.cvtColor(img2,cv2.COLOR_RGB2HSV)  #將圖片從RGB轉換為HSV色彩空間

while True:
    h_min = cv2.getTrackbarPos('Hue min', 'trackBar')  #獲取Hue min值
    h_max = cv2.getTrackbarPos('Hue max', 'trackBar')  #獲取Hue max值
    s_min = cv2.getTrackbarPos('sat min', 'trackBar')  #獲取saturation min值
    s_max = cv2.getTrackbarPos('sat max', 'trackBar')  #獲取saturation max值
    v_min = cv2.getTrackbarPos('val min', 'trackBar')  #獲取value min值
    v_max = cv2.getTrackbarPos('val max', 'trackBar')  #獲取value max值
    #print(h_min, h_max, s_min, s_max, v_min, v_max)  #打印滑桿的值
    lower = np.array([h_min, s_min, v_min])  #存放色相、飽和度、明度的最小值（下限）
    upper = np.array([h_max, s_max, v_max])  #存放色相、飽和度、明度的最大值（上限）
    
    mask = cv2.inRange(hsv, lower,upper)  #根據滑桿的值篩選顏色
    result = cv2.bitwise_and(img2, img2, mask=mask)  #將篩選後的顏色與原圖進行按位與操作
    cv2.imshow("mask", mask)  #顯示轉換後的圖片
    cv2.imshow("result", result)  #顯示篩選後的圖片
    cv2.waitKey(1)
    