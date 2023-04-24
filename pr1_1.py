import cv2
import numpy as np
import matplotlib.pyplot as plt

arr1=(np.ones((2,3,1))*255).astype(np.uint8)
arr2=np.zeros((2,3,1)).astype(np.uint8)
arr3=arr2.copy()

img=np.concatenate((arr3 , arr2 , arr1) , 2)
# print(arr1)
# print(img)
img_resize=cv2.resize(img ,(300,400))

cv2.imshow("imgage" , img_resize)
cv2.waitKey(0)