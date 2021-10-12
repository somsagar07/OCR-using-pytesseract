# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:33:53 2021

@author: Sagar
"""
import pytesseract 
import cv2

pytesseract.pytesseract.tesseract_cmd= 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('12.JPG')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

ht,wd,_ = img.shape

border = pytesseract.image_to_data(img)
for j,i in enumerate(border.splitlines()):
    if j!=0:
        i=i.split()
        if len(i)==12:
            a,b,c,d=int(i[6]),int(i[7]),int(i[8]),int(i[9]) 
            cv2.rectangle(img,(a,b),(c+a,d+b),(0,0,255),1)
            cv2.putText(img,i[11],(a,b),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    
cv2.imshow('Result',img)  
cv2.waitKey(0)
cv2.destroyAllWindows()