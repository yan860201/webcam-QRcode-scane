import numpy as np
import cv2
from pyzbar import pyzbar


video = cv2.VideoCapture(0)
dataList = [0]
while True:
    tof, img = video.read()
    h, w = (200, 200)
    x, y = (int((img.shape[1]-w)/2), int((img.shape[0]-h)/2))
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
    qrcode = pyzbar.decode(img[y:y+h, x:x+w, :])
    if len(qrcode)<2:
        for d in qrcode:
            if d.data != dataList[0]:
                dataList[0] = d.data
                print(dataList)
                print("類型:", d.type, "內容:", d.data.decode("UTF-8"))
            else:
                continue
    else:
        print("more then one code")
       
    cv2.imshow("0", img)
    cv2.waitKey(50)
cv2.destoryAllwindows()