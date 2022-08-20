import os.path

import cv2
eyee = cv2.CascadeClassifier('C:/Bangkit_Baru/baru/CAPSTONE_LATIHAN/haarcascade_eye.xml')
face = cv2.CascadeClassifier('C:/Bangkit_Baru/baru/CAPSTONE_LATIHAN/haarcascade_frontalface_default.xml')
gambar = cv2.imread('C:/Bangkit_Baru/baru/CAPSTONE_LATIHAN/IMG_20220504_094441.jpg')
gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
faces = face.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(gambar, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = gambar[y:y + h, x:x + w]
    eyes = eyee.detectMultiScale(roi_gray)
    i = 0
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        crop_img = roi_color[ey:ey + eh, ex:ex + ew]
        #cv2.imshow('gambar', crop_img)
        cv2.imwrite('C:/Bangkit_Baru/baru/CAPSTONE_LATIHAN/Cropeye/gambar{}.png'.format(i), crop_img)
        i += 1
cv2.waitKey(0)
cv2.destroyAllWindows()
