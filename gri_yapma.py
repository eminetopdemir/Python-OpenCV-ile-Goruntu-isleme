import cv2
import numpy as np

path = "doga.jpg" 
img = cv2.imread(path) 

if img is None:
    print("Görüntü bulunamadı, dosya yolunu kontrol edin.")
    exit()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", img)
cv2.imshow("Gray", imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()
