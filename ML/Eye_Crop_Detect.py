import cv2
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
baris = 5
kolom = 5
index = 0
fig = plt.gcf()
fig.set_size_inches(baris*5, kolom*5)
index += 10
direktori_path = 'D:/archive(11)'
train_1 = os.path.join(direktori_path, 'thispersondoesnotexist.10k')
#train_1_1 = os.path.join(train_1, 'train_1')
eyee = cv2.CascadeClassifier('C:/Bangkit_Baru/baru/CAPSTONE_LATIHAN/haarcascade_eye.xml')
face = cv2.CascadeClassifier('C:/Bangkit_Baru/baru/CAPSTONE_LATIHAN/haarcascade_frontalface_default.xml')
new = []
for nama in os.listdir(train_1)[5000:10000]:
    gambar = cv2.imread('D:/archive(11)/thispersondoesnotexist.10k/{}'.format(nama))
    gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        #cv2.rectangle(gambar, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = gambar[y:y + h, x:x + w]
        eyes = eyee.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            crop_img = roi_color[ey:ey + eh, ex:ex + ew]
    cv2.imshow()
            #cv2.imwrite('{}'.format(nama), crop_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
