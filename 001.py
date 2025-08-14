import cv2 #測試讀取相片

# 1. 讀取圖片 
img = cv2.imread("test.jpg")

# 檢查是否讀取成功
if img is None:
    print("無法讀取圖片，請檢查路徑！")
    exit()

# 2. 顯示原圖
cv2.imshow("Original", img)

# 3. 轉成灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# 4. 儲存處理後的圖片
cv2.imwrite("gray_output.jpg", gray)

# 5. 等待按鍵後關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
